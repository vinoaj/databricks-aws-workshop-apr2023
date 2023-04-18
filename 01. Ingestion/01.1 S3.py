# Databricks notebook source
# MAGIC %md
# MAGIC # Ingesting data from S3
# MAGIC 
# MAGIC This Notebook will walk you through patterns for ingesting data from S3. This is often the first step in a batch ETL pipeline to ingest and process raw data
# MAGIC 
# MAGIC Your cluster has an [instance profile](https://docs.databricks.com/aws/iam/instance-profile-tutorial.html) attached to it that gives it the required privileges to read from and write to the appropriate S3 buckets

# COMMAND ----------

# MAGIC %md
# MAGIC # Initialisation
# MAGIC 
# MAGIC ## Load widgets
# MAGIC 
# MAGIC [Widgets](https://docs.databricks.com/notebooks/widgets.html) are a convenient way to paramaterize your Notebook code by providing users input controls above 👆🏽

# COMMAND ----------

# To reset the data and restart the demo from scratch, switch the widget to True and run the "%run ./_resources/00-setup $reset_all_data=$reset_all_data" cell below.
dbutils.widgets.dropdown("reset_all_data", "false", ["true", "false"], "Reset all data")
dbutils.widgets.text("cloud_storage_path", "s3://{bucket_name}", "S3 Bucket")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Obtain the S3 bucket name from the AWS Console
# MAGIC 
# MAGIC - Go to your [AWS Account console to look up the S3 bucket](https://s3.console.aws.amazon.com/s3/buckets) for your workspace
# MAGIC - The bucket name will look like : `db-workshop-376145009885-ap-southeast-2-0d54ddd0`
# MAGIC - Insert your bucket name in the widget above 👆🏽
# MAGIC 
# MAGIC Now let's set up your schema (database). Note: we are using the `%run` command to execute another Notebook (alternatively we could import a Python script and run that instead)

# COMMAND ----------

# MAGIC %run ../_resources/00-setup $reset_all_data=$reset_all_data $cloud_storage_path=$cloud_storage_path

# COMMAND ----------

# MAGIC %md
# MAGIC ## Unity Catalog: catalogs and schemas
# MAGIC 
# MAGIC For this workshop, a catalog called `aws_dbx_workshop` has already been set up by the administrators and you have been given full access to it. Your schemas (databases) will live in this catalog.
# MAGIC 
# MAGIC Because we're using a shared Unity Catalog Metastore across the entire organisation (i.e. this event), you'll also be able to see schemas belonging to your fellow event participants. With UC you can control who has access and privileges to specific resources. However, for the purposes of this workshop everyone has full rights to the catalog (use your power wisely!)

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW CATALOGS;

# COMMAND ----------

# MAGIC %sql
# MAGIC USE CATALOG aws_dbx_workshop;
# MAGIC SHOW SCHEMAS; -- Let's look at all the schemas (databases) in this catalog

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT CURRENT_CATALOG() AS current_catalog, CURRENT_SCHEMA() AS current_schema

# COMMAND ----------

# MAGIC %md
# MAGIC We can get the results of a SQL query as a DataFrame by taking a copy of the `_sqldf` variable that accompanies every SQL execution

# COMMAND ----------

df_current = _sqldf
display(df_current)

current_catalog = df_current.first()["current_catalog"]
current_schema = df_current.first()["current_schema"]
print(f"Current CATALOG: {current_catalog}")
print(f"Current SCHEMA: {current_schema}")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Load data into S3 to simulate incoming new data
# MAGIC 
# MAGIC We'll simulate new incoming data into S3 by copying files from the `/databricks-datasets/` folder. This dataset is hosted by Databricks but accessible via any Workspace

# COMMAND ----------

# MAGIC %run ../_resources/00-basedata $reset_all_data=$reset_all_data

# COMMAND ----------

# MAGIC %md
# MAGIC # Let's use DBUtils to explore a Bucket
# MAGIC 
# MAGIC `dbutils` is a utility library in Databricks that simplifies common tasks such as managing databases, file systems, and notebooks
# MAGIC 
# MAGIC Databricks Documentation
# MAGIC 
# MAGIC - Databricks Utils https://docs.databricks.com/dev-tools/databricks-utils.html
# MAGIC - Working with S3 https://docs.databricks.com/external-data/amazon-s3.html

# COMMAND ----------

# DBTITLE 1,List files using dbutils
path = f"{cloud_storage_path}/ingest"
print(f"Listing path: {path}")

display(dbutils.fs.ls(path))

# COMMAND ----------

# DBTITLE 1,Read all files into DataFrame
path = f"{cloud_storage_path}/ingest"
print(f"Loading contents of {path} into a DataFrame")

df = spark.read.format("json").load(path)

df.display()
df.count()

# COMMAND ----------

# DBTITLE 1,Read a specific file into a DataFrame
path = f"{cloud_storage_path}/ingest"
first_file = dbutils.fs.ls(path)[0][0]

print(f"Loading file into DataFrame: {first_file}")
df = spark.read.format("json").load(first_file)

df.display()
df.count()

# COMMAND ----------

# DBTITLE 1,Read a specific file into a DataFrame and add Metadata
path = f"{cloud_storage_path}/ingest"
first_file = dbutils.fs.ls(path)[0][0]

# _metadata is an automatically generated column that contains metadata about the JSON structure 
#  and data types in the input file, which can be helpful for schema inference and data processing
df = spark.read.format("json").load(first_file).select("*", "_metadata")

df.display()

# COMMAND ----------

# DBTITLE 1,We can even read S3 buckets in other accounts
# Amazon Customer Reviews public dataset (https://s3.amazonaws.com/amazon-reviews-pds/readme.html)
S3_PATH_PARQUET = "s3://amazon-reviews-pds/parquet/"
display(dbutils.fs.ls(S3_PATH_PARQUET))

# COMMAND ----------

# MAGIC %md
# MAGIC # Using SQL inside a Python Notebook
# MAGIC 
# MAGIC Databricks Notebooks are **polyglot** notebooks, meaning that you can mix and match `Python`, `SQL`, `Scala`, and `R` in the same place!
# MAGIC 
# MAGIC To use SQL with a DataFrame, we first create a temporary view. We can then apply SQL queries against that view

# COMMAND ----------

# DBTITLE 1,Create a Temporary View
path = f"{cloud_storage_path}/ingest"

df = spark.read.format("json").load(dbutils.fs.ls(path)[0][0]).select("*", "_metadata")
df.createOrReplaceTempView("vw_json_files")

# COMMAND ----------

# DBTITLE 1,Query the Temporary View
# MAGIC %sql
# MAGIC SELECT * FROM vw_json_files LIMIT 10

# COMMAND ----------

# DBTITLE 1,Read files using SQL
# MAGIC %sql
# MAGIC SELECT * FROM JSON.`${cloud_storage_path}/ingest`

# COMMAND ----------

# DBTITLE 1,Create a Delta Table from Files
# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE iot_data
# MAGIC AS SELECT * 
# MAGIC FROM JSON.`${cloud_storage_path}/ingest`

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW TABLES

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT SUM(calories_burnt) AS total_calories 
# MAGIC FROM iot_data

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC 
# MAGIC # What is Databricks Auto Loader?
# MAGIC 
# MAGIC <img src="https://github.com/QuentinAmbard/databricks-demo/raw/main/product_demos/autoloader/autoloader-edited-anim.gif" style="float:right; margin-left: 10px" />
# MAGIC 
# MAGIC [Databricks Auto Loader](https://docs.databricks.com/ingestion/auto-loader/index.html) lets you scan a cloud storage folder (S3, ADLS, GCS) and only ingest the new data that arrived since the previous run.
# MAGIC 
# MAGIC This is called **incremental ingestion**.
# MAGIC 
# MAGIC Auto Loader can be used in a near real-time stream or in a batch fashion, e.g., running every night to ingest daily data.
# MAGIC 
# MAGIC Auto Loader provides a strong gaurantee when used with a Delta sink (the data will only be ingested once).
# MAGIC 
# MAGIC ## How Auto Loader simplifies data ingestion
# MAGIC 
# MAGIC Ingesting data at scale from cloud storage can be really hard at scale. Auto Loader makes it easy, offering these benefits:
# MAGIC 
# MAGIC 
# MAGIC * **Incremental** & **cost-efficient** ingestion (removes unnecessary listing or state handling)
# MAGIC * **Simple** and **resilient** operation: no tuning or manual code required
# MAGIC * Scalable to **billions of files**
# MAGIC   * Using incremental listing (recommended, relies on filename order)
# MAGIC   * Leveraging notification + message queue (when incremental listing can't be used)
# MAGIC * **Schema inference** and **schema evolution** are handled out of the box for most formats (csv, json, avro, images...)
# MAGIC 
# MAGIC <img width="1px" src="https://www.google-analytics.com/collect?v=1&gtm=GTM-NKQ8TT7&tid=UA-163989034-1&cid=555&aip=1&t=event&ec=field_demos&ea=display&dp=%2F42_field_demos%2Ffeatures%2Fauto_loader%2Fnotebook&dt=FEATURE_AUTOLOADER">

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC 
# MAGIC ## Using Auto Loader
# MAGIC 
# MAGIC In the cell below, a function is defined to demonstrate using Databricks Auto Loader with the PySpark API. This code includes both a Structured Streaming read and write.
# MAGIC 
# MAGIC The following notebook will provide a more robust overview of Structured Streaming. If you wish to learn more about Auto Loader options, refer to the <a href="https://docs.databricks.com/spark/latest/structured-streaming/auto-loader.html" target="_blank">documentation</a>.
# MAGIC 
# MAGIC Note that when using Auto Loader with automatic <a href="https://docs.databricks.com/spark/latest/structured-streaming/auto-loader-schema.html" target="_blank">schema inference and evolution</a>, the 4 arguments shown here should allow ingestion of most datasets. These arguments are explained below.
# MAGIC 
# MAGIC | argument | what it is | how it's used |
# MAGIC | --- | --- | --- |
# MAGIC | **`data_source`** | The directory of the source data | Auto Loader will detect new files as they arrive in this location and queue them for ingestion; passed to the **`.load()`** method |
# MAGIC | **`source_format`** | The format of the source data |  While the format for all Auto Loader queries will be **`cloudFiles`**, the format of the source data should always be specified for the **`cloudFiles.format`** option |
# MAGIC | **`table_name`** | The name of the target table | Spark Structured Streaming supports writing directly to Delta Lake tables by passing a table name as a string to the **`.table()`** method. Note that you can either append to an existing table or create a new table |
# MAGIC | **`checkpoint_directory`** | The location for storing metadata about the stream | This argument is passed to the **`checkpointLocation`** and **`cloudFiles.schemaLocation`** options. Checkpoints keep track of streaming progress, while the schema location tracks updates to the fields in the source dataset |
# MAGIC 
# MAGIC **NOTE**: The code below has been streamlined to demonstrate Auto Loader functionality. We'll see in later lessons that additional transformations can be applied to source data before saving them to Delta Lake.

# COMMAND ----------

# DBTITLE 1,Use Autoloader to Read Cloud Files as a Stream
schema_location = f"{cloud_storage_path}/ingest/schema"

bronzeDF = (
    spark.readStream.format("cloudFiles")
    .option("cloudFiles.format", "json")
    .option("cloudFiles.maxFilesPerTrigger", 1)  # demo only, remove in real stream. Default is 1000
    .option("cloudFiles.schemaLocation", schema_location)
    .option("rescuedDataColumn", "_rescue")  # data that does not match schema is placed in _rescue column
    #.schema("address string") # you can provide schema hints
    .load(f"{cloud_storage_path}/ingest/")
    .select("*", "_metadata")  # add metadata to bronze so we know the source files etc
)

# COMMAND ----------

(
bronzeDF.writeStream
    .option("checkpointLocation", f"{cloud_storage_path}/bronze/bronze_iot_stream/checkpoint")
    .trigger(once=True)
    .option("mergeSchema", "true")
    .table(f"{current_catalog}.{current_schema}.iot_autoloader_demo") # table name
)

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW TABLES

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT COUNT(*) FROM iot_autoloader_demo

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM iot_autoloader_demo

# COMMAND ----------

# DBTITLE 1,Check Files State in the Checkpoint
# MAGIC %sql
# MAGIC SELECT * FROM cloud_files_state("${cloud_storage_path}/bronze/bronze_iot_stream/checkpoint");

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT DISTINCT _metadata FROM iot_autoloader_demo

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE HISTORY iot_autoloader_demo

# COMMAND ----------

# DBTITLE 1,Add more Data
file_counter = add_data(file_counter)

# Go To CMD #28 to re-run Auto Loader

# COMMAND ----------

# MAGIC %md
# MAGIC [Documentation: `OPTIMIZE`](https://docs.databricks.com/delta/optimize.html)
# MAGIC 
# MAGIC Delta Lake on Databricks can improve the speed of read queries from a table. One way to improve this speed is to coalesce small files into larger ones

# COMMAND ----------

# DBTITLE 0,Optimize table
# MAGIC %sql
# MAGIC OPTIMIZE iot_autoloader_demo

# COMMAND ----------

# MAGIC %md
# MAGIC [Documentation: `ANALYZE`](https://docs.databricks.com/sql/language-manual/sql-ref-syntax-aux-analyze-table.html)
# MAGIC 
# MAGIC The ANALYZE TABLE statement collects statistics about one specific table or all the tables in one specified schema, that are to be used by the query optimizer to find a better query execution plan

# COMMAND ----------

# MAGIC %sql
# MAGIC ANALYZE TABLE iot_autoloader_demo COMPUTE STATISTICS

# COMMAND ----------

# MAGIC %md
# MAGIC # Brief Detour: Delta Lake
# MAGIC 
# MAGIC Let's take a brief detour to look at some interesting aspects of Delta Lake tables

# COMMAND ----------

# MAGIC %md
# MAGIC ## Time Travel
# MAGIC 
# MAGIC Let's start with **time travel**. You've seen `DESCRIBE HISTORY` which shows the order of operations applied to your table. Now let's look at [time travelling](https://docs.databricks.com/delta/history.html) to view your table at a previous state 

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM iot_autoloader_demo VERSION AS OF 2;

# COMMAND ----------

# MAGIC %sql
# MAGIC -- UTC time; change this to 5 date and time of 5 minutes ago
# MAGIC SELECT * FROM iot_autoloader_demo TIMESTAMP AS OF "2023-04-17T08:45:00.000Z"

# COMMAND ----------

# MAGIC %md
# MAGIC ## Change Data Feed
# MAGIC 
# MAGIC [Change data feed](https://docs.databricks.com/delta/delta-change-data-feed.html) allows Databricks to track row-level changes between versions of a Delta table. When enabled on a Delta table, the runtime records change events for all the data written into the table. This includes the row data along with metadata indicating whether the specified row was inserted, deleted, or updated

# COMMAND ----------

# MAGIC %sql
# MAGIC ALTER TABLE iot_autoloader_demo SET TBLPROPERTIES (delta.enableChangeDataFeed = true);
# MAGIC 
# MAGIC -- Note down which version for which the activation of change data feed occured
# MAGIC DESCRIBE HISTORY iot_autoloader_demo;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM TABLE_CHANGES("iot_autoloader_demo", 7, 10);

# COMMAND ----------

# DBTITLE 1,Load additional data
file_counter = add_data(file_counter)

(
bronzeDF.writeStream
    .option("checkpointLocation", f"{cloud_storage_path}/bronze/bronze_iot_stream/checkpoint")
    .trigger(once=True)
    .option("mergeSchema", "true")
    .table(f"{current_catalog}.{current_schema}.iot_autoloader_demo") # table name
)

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC -- Let's also update & delete some rows
# MAGIC UPDATE iot_autoloader_demo SET user_id = 37 WHERE user_id = 7;
# MAGIC DELETE FROM iot_autoloader_demo WHERE user_id = 37;
# MAGIC 
# MAGIC SELECT * FROM TABLE_CHANGES("iot_autoloader_demo", 7, 10);

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM table_changes("iot_autoloader_demo", 7, 99) WHERE _change_type LIKE "%update%"

# COMMAND ----------

# MAGIC %md
# MAGIC # Ingesting a high volume of input files
# MAGIC Scanning folders with many files to detect new data is an expensive operation, leading to ingestion challenges and higher cloud storage costs.
# MAGIC 
# MAGIC To solve this issue and support an efficient listing, Databricks autoloader offers two modes:
# MAGIC 
# MAGIC - Incremental listing with `cloudFiles.useIncrementalListing` (recommended), based on the alphabetical order of the file's path to only scan new data: (`ingestion_path/YYYY-MM-DD`)
# MAGIC - Notification system, which sets up a managed cloud notification system sending new file name to a queue (when we can't rely on file name order). See `cloudFiles.useNotifications` for more details.
# MAGIC 
# MAGIC <img src="https://github.com/QuentinAmbard/databricks-demo/raw/main/product_demos/autoloader-mode.png" width="700"/>
# MAGIC 
# MAGIC Use the incremental listing option whenever possible. Databricks Auto Loader will try to auto-detect and use the incremental approach when possible.

# COMMAND ----------

bronzeDF = (
    spark.readStream.format("cloudFiles")
    .option("cloudFiles.format", "json")
    .option(
        "cloudFiles.schemaLocation", f"{cloud_storage_path}/auto_loader/inferred_schema"
    )
    .option("cloudFiles.inferColumnTypes", "true")
    .option("cloudfiles.useNotifications", "true")
    .option(
        "cloudFiles.backfillInterval", "1 week"
    )  # Auto Loader can trigger asynchronous backfills at a given interval, e.g. 1 day to backfill once a day, or 1 week
    .load(f"{cloud_storage_path}/ingest_sns")
)

# COMMAND ----------

bronzeDF.writeStream.format("delta").option(
    "checkpointLocation",
    f"{cloud_storage_path}/bronze/bronze_iot_sns_stream/checkpoint",
).trigger(once=True).option("mergeSchema", "true").outputMode("append").table(
    f"{current_catalog}.{current_schema}.iot_autoloader_demo_sns" # table name
)

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM cloud_files_state("${cloud_storage_path}/bronze/bronze_iot_sns_stream/checkpoint");

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE HISTORY iot_autoloader_demo_sns;

# COMMAND ----------

# DBTITLE 1,Add More files
file_counter_sns = move_file_sns(file_counter_sns)

display(dbutils.fs.ls(f"{cloud_storage_path}/ingest_sns"))

# COMMAND ----------

# MAGIC %md
# MAGIC # Support for images
# MAGIC Databricks Auto Loader provides native support for images and binary files.
# MAGIC 
# MAGIC <img src="https://github.com/QuentinAmbard/databricks-demo/raw/main/product_demos/autoloader-images.png" width="800" />
# MAGIC 
# MAGIC Just set the format accordingly and the engine will do the rest: `.option("cloudFiles.format", "binaryFile")`
# MAGIC 
# MAGIC Use-cases:
# MAGIC 
# MAGIC - ETL images into a Delta table using Auto Loader
# MAGIC - Automatically ingest continuously arriving new images
# MAGIC - Easily retrain ML models on new images
# MAGIC - Perform distributed inference using a pandas UDF directly from Delta

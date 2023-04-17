# databricks-aws-workshop-apr2023

Link to this repo: <https://github.com/vinoaj/databricks-aws-workshop-apr2023>

## Additional Notebooks

If you enjoyed this workshop and are looking for other workshop Notebooks to experiment with, check out these repos:

- [Databricks Demos: dbdemos.ai](https://www.dbdemos.ai/index.html): install and run demos in your Workspace
- [📄 Databricks Academy lab notebooks](https://github.com/databricks-academy)
- [📄 ANZ Bootcamp notebooks](https://github.com/zivilenorkunaite/apjbootcamp2023)
- [📄 Databricks Industry Solutions notebooks](https://github.com/databricks-industry-solutions)
- [Notebook gallery](https://github.com/databricks/notebook_gallery)

## Keep Current and Learning Resources

### News and Learning Content

[▶️ YouTube channel](https://www.youtube.com/channel/UC3q8O3Bh2Le8Rj1-Q-_UUbA) | [🎧 Data Brew Podcast](https://databricks.com/discover/data-brew) | [📖 Databricks Blog](https://databricks.com/blog)

- [▶️ Data + AI Summit (DAIS) 2022 recordings](https://www.youtube.com/playlist?list=PLTPXxbhUt-YVWi_cf2UUDc9VZFLoRgu0l)
- [Free Live Onboarding Training](https://files.training.databricks.com/static/ilt-sessions/onboarding/index.html): no-cost, role-based onboarding training, multiple times a day across key geographic regions for Databricks customers, partners, as well as the general public

## Lakehouse Paradigm

- [Lakehouse: A New Generation of Open Platforms that Unify Data Warehousing and Advanced Analytics](http://www.cidrdb.org/cidr2021/papers/cidr2021_paper17.pdf) Research paper from the 11th Annual Conference on Innovative Data Systems Research (CIDR ’21), January 11–15, 2021. My [annotated version](assets/cidr2021_paper17_vinoaj_annotated.pdf)

---

## AWS-specific content

### Architecture

- [Leveraging Delta Across Teams at McGraw Hill](https://www.databricks.com/blog/2022/09/14/leveraging-delta-across-teams-mcgraw-hill.html) ([source code](https://github.com/MHEducation/databricks-athena-blog-code) to automate the Databricks to Athena manifest based integration)
![McGraw Hill architecture](https://cms.databricks.com/sites/default/files/inline-images/db-302-blog-img-4.png)

### Deployment

- [Best Practices and Guidance for Cloud Engineers to Deploy Databricks on AWS: Part 1](https://www.databricks.com/blog/2022/09/30/best-practices-and-guidance-cloud-engineers-deploy-databricks-aws-part-1.html), [Part 2](https://www.databricks.com/blog/2023/01/27/best-practices-and-guidance-cloud-engineers-deploy-databricks-aws-part-2.html)
- [Optimizing AWS S3 Access for Databricks](https://www.databricks.com/blog/2022/11/08/optimizing-aws-s3-access-databricks.html)
- [Terraform script example (unofficial)](https://github.com/LeoneGarage/terraform)
- [Terraform script example (unofficial)](https://github.com/LeoneGarage/AWS-ISV-Summit-Provision)
- [▶️ Deploying Databricks on the AWS Marketplace](https://www.youtube.com/watch?v=gU1BrfqMCYc)
- [AWS Quickstart](https://aws.amazon.com/quickstart/architecture/databricks/)
- [CloudFormation custom resources to wrap the Databricks API](https://github.com/ioannisatdatabricks/databricks_deployments_on_aws)

### ETL / ELT

#### Ingestion: Streaming

- [Enhanced Fan-Out for Kinesis on Databricks](https://www.databricks.com/blog/2023/01/31/announcing-support-enhanced-fan-out-kinesis-databricks.html)

### Guides

- [Build an MLOps sentiment analysis pipeline using Amazon SageMaker Ground Truth and Databricks MLflow](https://aws.amazon.com/blogs/machine-learning/build-an-mlops-sentiment-analysis-pipeline-using-amazon-sagemaker-ground-truth-and-databricks-mlflow/)

### Migration

- [How to Migrate Your Data and AI Workloads to Databricks With the AWS Migration Acceleration Program](https://www.databricks.com/blog/2022/08/19/how-to-migrate-your-data-and-ai-workloads-to-databricks-with-the-aws-migration-acceleration-program.html)
- [Migrating Transactional Data to a Delta Lake using AWS DMS](https://www.databricks.com/blog/2019/07/15/migrating-transactional-data-to-a-delta-lake-using-aws-dms.html)
- [Using Streaming Delta Live Tables and AWS DMS for Change Data Capture From MySQL](https://www.databricks.com/blog/2022/09/29/using-streaming-delta-live-tables-and-aws-dms-change-data-capture-mysql.html)

### Security

- [Using Enhanced Security Monitoring to Detect & Alert for Suspicious Activity on Your Databricks Clusters](https://www.databricks.com/blog/2022/09/01/using-enhanced-security-monitoring-detect-alert-suspicious-activity-your-databricks)

---

## Deployment Architecture & Management

### Architecture & Data Model Design

- [6 Guiding Principles to Build an Effective Data Lakehouse](https://databricks.com/blog/2022/07/14/6-guiding-principles-to-build-an-effective-data-lakehouse.html)
- [Data Warehousing Modeling Techniques and Their Implementation on the Databricks Lakehouse Platform](https://databricks.com/blog/2022/06/24/data-warehousing-modeling-techniques-and-their-implementation-on-the-databricks-lakehouse-platform.html)
- [Five Simple Steps for Implementing a Star Schema in Databricks With Delta Lake](https://databricks.com/blog/2022/05/20/five-simple-steps-for-implementing-a-star-schema-in-databricks-with-delta-lake.html)
- [Databricks Lakehouse and Data Mesh, (Part 1)](https://www.databricks.com/blog/2022/10/10/databricks-lakehouse-and-data-mesh-part-1.html) [(Part 2)](https://www.databricks.com/blog/2022/10/19/building-data-mesh-based-databricks-lakehouse-part-2.html)
![Data Mesh architecture](https://cms.databricks.com/sites/default/files/inline-images/db-363-blog-image-3.png)
- [Dimensional modeling implementation on the modern lakehouse using Delta Live Tables](https://www.databricks.com/blog/2022/11/07/load-edw-dimensional-model-real-time-databricks-lakehouse.html): covers SCD1 & SCD2, PK/FK constraints, IDENTITY columns, and constraints ([📄 Notebook](https://github.com/dbsys21/databricks-lakehouse/blob/main/lakehouse-buildout/dimensional-modeling/E2E-Dimensional-Modeling-DLT.sql))
- [Prescriptive Guidance for Implementing a Data Vault Model on the Databricks Lakehouse Platform](https://databricks.com/blog/2022/06/24/prescriptive-guidance-for-implementing-a-data-vault-model-on-the-databricks-lakehouse-platform.html)
- [Architecting MLOps on the Lakehouse](https://databricks.com/blog/2022/06/22/architecting-mlops-on-the-lakehouse.html)
- [Leveraging Delta Across Teams at McGraw Hill](https://www.databricks.com/blog/2022/09/14/leveraging-delta-across-teams-mcgraw-hill.html) ([source code](https://github.com/MHEducation/databricks-athena-blog-code) to automate the Databricks to Athena manifest based integration)
![McGraw Hill architecture](https://cms.databricks.com/sites/default/files/inline-images/db-302-blog-img-4.png)

### Administration

- [Databricks Workspace Administration – Best Practices for Account, Workspace and Metastore Admins](https://www.databricks.com/blog/2022/08/26/databricks-workspace-administration-best-practices-for-account-workspace-and-metastore-admins.html)
- [Functional Workspace Organization on Databricks](https://databricks.com/blog/2022/03/10/functional-workspace-organization-on-databricks.html) (Databricks Admin Essentials: Blog 1/5)
- [Monitoring Your Databricks Lakehouse Platform with Audit Logs](https://databricks.com/blog/2022/05/02/monitoring-your-databricks-lakehouse-platform-with-audit-logs.html) (Databricks Admin Essentials: Blog 2/5) ([Notebook](https://github.com/andyweaves/databricks-audit-logs))
- [Serving Up a Primer for Unity Catalog Onboarding](https://www.databricks.com/blog/2022/11/22/serving-primer-unity-catalog-onboarding.html) (Databricks Admin Essentials)

#### Cost Management

- [Best Practices for Cost Management on Databricks](https://www.databricks.com/blog/2022/10/18/best-practices-cost-management-databricks.html)

### Unity Catalog 🔐

- [Serving Up a Primer for Unity Catalog Onboarding](https://www.databricks.com/blog/2022/11/22/serving-primer-unity-catalog-onboarding.html) (Databricks Admin Essentials)
- [How Terraform can enable Unity Catalog deployment at scale for different governance models](https://www.databricks.com/blog/2022/12/08/automated-guide-distributed-and-decentralized-management-unity-catalog.html)
- [Terraform scripts](https://github.com/databricks/unity-catalog-setup)
- [▶️ https://www.youtube.com/watch?v=l_fZ7RFOf_s](https://www.youtube.com/watch?v=l_fZ7RFOf_s)
- [Export lineage via API](https://github.com/databricks/unity-catalog-setup/blob/main/lineage/lineage_export.py) example

## Under the Hood: Photon Engine

- [Photon: A Fast Query Engine for Lakehouse Systems](https://www-cs.stanford.edu/~matei/papers/2022/sigmod_photon.pdf): SIGMOD 2022 Paper
- [Apache Spark and Photon Receive SIGMOD Awards](https://databricks.com/blog/2022/06/15/apache-spark-and-photon-receive-sigmod-awards.html)
- [▶️ Advancing Spark - The Photon Whitepaper](https://www.youtube.com/watch?v=hxvQxI4FksY)
- [How DuPont achieved 11x latency reduction and 4x cost reduction with Photon](https://www.databricks.com/blog/2022/10/04/how-dupont-achieved-11x-latency-reduction-and-4x-cost-reduction-photon.html)

## Under the Hood: Delta Lake

<img src="https://docs.delta.io/latest/_static/delta-lake-white.png" width="100" alt="Delta Lake Logo"></img>

- [Releases](https://github.com/delta-io/delta/releases)
- [Release Milestones](https://github.com/delta-io/delta/milestones)
- [Delta Transactional Log Protocol](https://github.com/delta-io/delta/blob/master/PROTOCOL.md)
- [📄 Delta Lake VLDB paper](https://databricks.com/wp-content/uploads/2020/08/p975-armbrust.pdf) (my [annotated version](../../assets/p975-armbrust_vinoaj_annotated.pdf))
- 📘 Delta Lake: The Definitive Guide (O'Reilly) ([access free preview](https://www.databricks.com/p/ebook/delta-lake-the-definitive-guide-by-oreilly) | [PDF direct link](https://www.databricks.com/wp-content/uploads/2021/05/9781098104528-1.pdf))
- [Diving Into Delta Lake: Unpacking The Transaction Log](https://www.databricks.com/blog/2019/08/21/diving-into-delta-lake-unpacking-the-transaction-log.html)
- [Diving Into Delta Lake: Schema Enforcement & Evolution](https://www.databricks.com/blog/2019/09/24/diving-into-delta-lake-schema-enforcement-evolution.html)
- [Diving Into Delta Lake: DML Internals (Update, Delete, Merge)](https://www.databricks.com/blog/2020/09/29/diving-into-delta-lake-dml-internals-update-delete-merge.html)
- [Processing Petabytes of Data in Seconds with Databricks Delta](https://www.databricks.com/blog/2018/07/31/processing-petabytes-of-data-in-seconds-with-databricks-delta.html)
- [Top 5 Reasons to Convert Your Cloud Data Lake to a Delta Lake](https://databricks.com/blog/2020/08/21/top-5-reasons-to-convert-your-cloud-data-lake-to-a-delta-lake.html)
- [How to Rollback a Delta Lake Table to a Previous Version with Restore](https://delta.io/blog/2022-10-03-rollback-delta-lake-restore/)
- [Exploring Delta Lake’s `ZORDER` and Performance](https://www.confessionsofadataguy.com/exploring-delta-lakes-zorder-and-performance-on-databricks/)
- [Idempotent Writes to Delta Lake Tables](https://towardsdatascience.com/idempotent-writes-to-delta-lake-tables-96f49addd4aa)

### Delta Sharing

- [GitHub repository](https://github.com/delta-io/delta-sharing)
- [Release Milestones](https://github.com/delta-io/delta-sharing/milestones)
- [▶️ Databricks Delta Sharing demo](https://www.youtube.com/watch?v=wRT1Vpbyy88)
- [▶️ PowerBI and Delta Sharing](https://www.linkedin.com/posts/dennyglee_powerbi-deltasharing-deltalake-activity-6988515550570196992-lsFw/?utm_source=share&utm_medium=member_ios)
- [▶️ Advancing Spark - Delta Sharing and Excel](https://www.youtube.com/watch?v=wRzx6GCiY70) (via PowerBI)
- [How Delta Sharing Helped Rearc Simplify Data Sharing and Maximize the Business Value of Its Data](https://www.databricks.com/blog/2022/09/13/how-delta-sharing-helped-rearc-simplify-data-sharing-and-maximize-business-value): With over 450+ open curated data products available across different sectors, Rearc's cross-industry catalog of datasets is one of the largest available today ([Rearc data library](https://www.rearc.io/data/delta-sharing/))

## ETL / ELT Patterns

### Ingestion

- [Auto-Loader](https://docs.databricks.com/spark/latest/structured-streaming/auto-loader.html)
- [Easy Ingestion to Lakehouse With `COPY INTO`](https://www.databricks.com/blog/2023/01/17/easy-ingestion-lakehouse-copy.html)
- [dbt](https://docs.databricks.com/dev-tools/dbt.html) ([GitHub](https://github.com/databricks/dbt-databricks))
- [▶️ dbt Projects Integration in Databricks Workflows](https://www.youtube.com/watch?v=C4-FOpJzhKs)
- [Best Practices for Super Powering Your dbt Project on Databricks](https://www.databricks.com/blog/2022/12/15/best-practices-super-powering-your-dbt-project-databricks.html)
- [Build Data and ML Pipelines More Easily With Databricks and Apache Airflow](https://databricks.com/blog/2022/04/29/build-data-and-ml-pipelines-more-easily-with-databricks-and-apache-airflow.html)
- [Ingesting emails (IMAP)](https://medium.com/@ottoli/automating-data-extraction-from-e-mail-attachments-with-databricks-6d74e4c68006)

### Ingestion: Streaming

- [Real-Time Insights: The Top Three Reasons Why Customers Love Data Streaming with Databricks](https://www.databricks.com/blog/2023/03/14/real-time-insights-top-three-reasons-why-customers-love-data-streaming.html)
- [Simplifying Streaming Data Ingestion into Delta Lake](https://www.databricks.com/blog/2022/09/12/simplifying-streaming-data-ingestion-delta-lake.html)
- [Streaming in Production: Collected Best Practices - Part 1](https://www.databricks.com/blog/2022/12/12/streaming-production-collected-best-practices.html), [Part 2](https://www.databricks.com/blog/2023/01/10/streaming-production-collected-best-practices-part-2.html)
- [Speed Up Streaming Queries With Asynchronous State Checkpointing](https://databricks.com/blog/2022/05/02/speed-up-streaming-queries-with-asynchronous-state-checkpointing.html)
- [Scalable Spark Structured Streaming for REST API Destinations](https://www.databricks.com/blog/2023/03/02/scalable-spark-structured-streaming-rest-api-destinations.html): How to use Spark Structured Streaming's foreachBatch to scalably publish data to REST APIs
- [Feature Deep Dive: Watermarking in Apache Spark Structured Streaming](https://www.databricks.com/blog/2022/08/22/feature-deep-dive-watermarking-in-apache-spark-structured-streaming.html)
- [Python Arbitrary Stateful Processing in Structured Streaming](https://www.databricks.com/blog/2022/10/18/python-arbitrary-stateful-processing-structured-streaming.html)
- Monitoring streaming queries ([PySpark](https://www.databricks.com/blog/2022/05/27/how-to-monitor-streaming-queries-in-pyspark.html) | [Scala](https://docs.databricks.com/structured-streaming/stream-monitoring.html#language-scala))
- [Using Spark Structured Streaming to Scale Your Analytics](https://www.databricks.com/blog/2022/07/14/using-spark-structured-streaming-to-scale-your-analytics.html)
- [State Rebalancing in Structured Streaming](https://www.databricks.com/blog/2022/10/04/state-rebalancing-structured-streaming.html)
- [▶️ Streaming data into the Lakehouse](https://www.youtube.com/watch?v=FFVH7G9iN68)
- [Simplifying Streaming Data Ingestion into Delta Lake](https://www.databricks.com/blog/2022/09/12/simplifying-streaming-data-ingestion-delta-lake.html)
![High level view of streaming data ingestion into delta lake](https://cms.databricks.com/sites/default/files/inline-images/db-265-blog-img-1.png)
- [Enhanced Fan-Out for Kinesis on Databricks](https://www.databricks.com/blog/2023/01/31/announcing-support-enhanced-fan-out-kinesis-databricks.html)
- Roadmap: [Project Lightspeed: Faster and Simpler Stream Processing With Apache Spark](https://www.databricks.com/blog/2022/06/28/project-lightspeed-faster-and-simpler-stream-processing-with-apache-spark.html)
- [Debugging using the Structured Streaming UI](https://www.databricks.com/blog/2020/07/29/a-look-at-the-new-structured-streaming-ui-in-apache-spark-3-0.html) ([Spark docs](https://spark.apache.org/docs/latest/web-ui.html#structured-streaming-tab))
- [Confluent Streaming for Databricks: Build Scalable Real-time Applications on the Lakehouse (Part I)](https://databricks.com/blog/2022/01/13/confluent-streaming-for-databricks-build-scalable-real-time-applications-on-the-lakehouse.html) [(Part II)](https://databricks.com/blog/2022/05/17/build-scalable-real-time-applications-on-the-lakehouse-using-confluent-databricks-part-2.html)

### Delta Live Tables (DLT)

- [Delta Live Tables Notebooks](https://github.com/databricks/delta-live-tables-notebooks)
- [Dimensional modeling implementation on the modern lakehouse using Delta Live Tables](https://www.databricks.com/blog/2022/11/07/load-edw-dimensional-model-real-time-databricks-lakehouse.html): covers SCD1 & SCD2, PK/FK constraints, IDENTITY columns, and constraints ([📄 Notebook](https://github.com/dbsys21/databricks-lakehouse/blob/main/lakehouse-buildout/dimensional-modeling/E2E-Dimensional-Modeling-DLT.sql))
- [Data Vault Best practice & Implementation on the Lakehouse](https://www.databricks.com/blog/2023/02/24/data-vault-best-practice-implementation-lakehouse.html)
- [Build a Customer 360 Solution with Fivetran and Delta Live Tables](https://www.databricks.com/blog/2022/11/09/build-customer-360-solution-fivetran-and-delta-live-tables.html) - includes SCD2 example
- [Simplifying Change Data Capture With Databricks Delta Live Tables](https://databricks.com/blog/2022/04/25/simplifying-change-data-capture-with-databricks-delta-live-tables.html)
- [Delivering Real-Time Data to Retailers with Delta Live Tables](https://databricks.com/blog/2022/04/12/delivering-real-time-data-to-retailers-with-delta-live-tables.html) (fully documented [notebooks](https://d1r5llqwmkrl74.cloudfront.net/notebooks/RCG/POS_DLT/index.html#POS_DLT_1.html))
- [Building ETL pipelines for the cybersecurity lakehouse with Delta Live Tables](https://databricks.com/blog/2022/06/03/building-etl-pipelines-for-the-cybersecurity-lakehouse-with-delta-live-tables.html): ingest & evaluate AWS CloudTrail & VPC Flow logs (accompanying notebooks: [CloudTrail DLT pipeline](https://databricks.com/wp-content/uploads/notebooks/db-172-dlt/cloudtrail-dlt-pipeline.html), [VPC Flow Logs DLT pipeline](https://databricks.com/wp-content/uploads/notebooks/db-172-dlt/vpc-flow-logs-dlt-pipeline.html), [Zeek DLT pipeline](https://databricks.com/wp-content/uploads/notebooks/db-172-dlt/zeek-dlt-pipeline.html))
- [Low-latency Streaming Data Pipelines with Delta Live Tables and Apache Kafka](https://www.databricks.com/blog/2022/08/09/low-latency-streaming-data-pipelines-with-delta-live-tables-and-apache-kafka.html)
- [▶️ Apache Kafka and Delta Live Tables](https://www.youtube.com/watch?v=ntbs0uwPvxY)
- [How I Built A Streaming Analytics App With SQL and Delta Live Tables](https://databricks.com/blog/2022/05/19/how-i-built-a-streaming-analytics-app-with-sql-and-delta-live-tables.html): accompanying [repo](https://github.com/databricks/delta-live-tables-notebooks/tree/main/divvy-bike-demo)
- [How Uplift built CDC and Multiplexing data pipelines with Databricks Delta Live Tables](https://databricks.com/blog/2022/04/27/how-uplift-built-cdc-and-multiplexing-data-pipelines-with-databricks-delta-live-tables.html)
- [Near Real-Time Anomaly Detection with Delta Live Tables and Databricks Machine Learning](https://www.databricks.com/blog/2022/08/08/near-real-time-anomaly-detection-with-delta-live-tables-and-databricks-machine-learning.html)
- [How Audantic Uses Databricks Delta Live Tables to Increase Productivity for Real Estate Market Segments](https://databricks.com/blog/2022/05/05/how-audantic-uses-databricks-delta-live-tables-to-increase-productivity-for-real-estate-market-segments.html)
![Audantic's Delta Live Tables Architecture](https://databricks.com/wp-content/uploads/2022/04/db-80-blog-img-2.png)

---

## Development

- [SQL CLI](https://docs.databricks.com/dev-tools/databricks-sql-cli.html): run SQL queries on your SQL endpoints from your terminal. From the command line, you get productivity features such as suggestions and syntax highlighting
- [sqlparse](https://github.com/andialbrecht/sqlparse): open source library for formatting and analysing SQL strings

---

## Orchestration

### Databricks Workflows

- [Databricks Workflows Through Terraform: Part I](https://www.databricks.com/blog/2022/12/5/databricks-workflows-through-terraform.html), [Part II](https://www.databricks.com/blog/2022/12/20/reuse-existing-workflows-through-terraform.html)
- [Why We Migrated From Apache Airflow to Databricks Workflows at YipitData](https://www.databricks.com/blog/2022/12/07/why-we-migrated-apache-airflow-databricks-workflows-yipitdata.html)
- [Save Time and Money on Data and ML Workflows With “Repair and Rerun”](https://databricks.com/blog/2022/05/06/save-time-and-money-on-data-and-ml-workflows-with-repair-and-rerun.html)

---

## DataOps

### IDEs

- [VS Code extension](https://marketplace.visualstudio.com/items?itemName=databricks.databricks) (short [▶️ video](https://www.youtube.com/watch?v=_QkcrYttVRs))
- [Use an IDE with Databricks](https://docs.databricks.com/dev-tools/ide-how-to.html#set-up-the-code-sample)
- [Software engineering best practices for notebooks](https://docs.databricks.com/notebooks/best-practices.html) ([accompanying notebooks](https://github.com/databricks/notebook-best-practices)) ([accompanying notebooks](https://github.com/databricks/ide-best-practices))
- [Build Reliable Production Data and ML Pipelines With Git Support for Databricks Workflows](https://databricks.com/blog/2022/06/21/build-reliable-production-data-and-ml-pipelines-with-git-support-for-databricks-workflows.html) ([📄 notebooks](https://github.com/RafiKurlansik/e2e-cuj))

### GitHub

- [GitHub Marketplace: Databricks](https://github.com/marketplace?query=databricks+publisher%3Adatabricks+)
- [GitHub Actions documentation](https://docs.databricks.com/dev-tools/ci-cd/ci-cd-github.html)

---

## Databricks SQL, Analysis & Business Intelligence (BI)

### SQL

- [What’s New With SQL User-Defined Functions](https://www.databricks.com/blog/2023/01/18/whats-new-sql-user-defined-functions.html) 2023-01-18

### ODBC & JDBC connectivity

- [Boosting Databricks ODBC Driver Performance](https://medium.com/creative-data/boosting-databricks-odbc-driver-be2cf08a7a4a)
- [Connect Excel to Databricks SQL Warehouse](https://medium.com/@fpatano/connect-excel-to-databricks-sql-warehouse-ec5b707c35e5)

### Analyst Experience

- [▶️ Low-Code Exploratory Data Analysis with Bamboolib](https://www.youtube.com/watch?v=VC9LxBwaPFw)

---

## Best Practices

- [Streaming in Production: Collected Best Practices - Part 1](https://www.databricks.com/blog/2022/12/12/streaming-production-collected-best-practices.html), [Part 2](https://www.databricks.com/blog/2023/01/10/streaming-production-collected-best-practices-part-2.html)
- [10 Best Practices for writing SQL in Databricks](https://medium.com/@fpatano/10-best-practices-for-writing-sql-in-databricks-7a445740e540)

### Performance tuning

- [Delta Lake best practices](https://docs.databricks.com/delta/best-practices.html)
- [Optimize performance with file management](https://docs.databricks.com/delta/optimizations/file-mgmt.html)
- [Make Your Data Lakehouse Run, Faster With Delta Lake 1.1](https://databricks.com/blog/2022/01/31/make-your-data-lakehouse-run-faster-with-delta-lake-1-1.html)
- [Get to Know Your Queries With the New Databricks SQL Query Profile](https://databricks.com/blog/2022/02/23/get-to-know-your-queries-with-the-new-databricks-sql-query-profile.html)
- [Top 5 Performance Tips](https://databricks.com/blog/2022/03/10/top-5-databricks-performance-tips.html)
- [Memory Profiling in PySpark](https://www.databricks.com/blog/2022/11/30/memory-profiling-pyspark.html)
- [How to consistently get the best performance from star schema databases](https://databricks.com/blog/2022/05/20/five-simple-steps-for-implementing-a-star-schema-in-databricks-with-delta-lake.html)
- [Delta – Best Practices for Managing Performance](https://daimlinc.com/blogs/data/delta-best-practices-for-managing-performance/) by partner Daimlinc
- [Introducing Ingestion Time Clustering with Databricks SQL and Databricks Runtime 11.2](https://www.databricks.com/blog/2022/11/18/introducing-ingestion-time-clustering-dbr-112.html): 19x faster query performance out-of-the-box. Write optimization, ensuring clustering is always maintained by ingestion time → significant query performance gains
- [Faster insights With Databricks Photon Using AWS i4i Instances With the Latest Intel Ice Lake Scalable Processors](https://www.databricks.com/blog/2022/09/13/faster-insights-databricks-photon-using-aws-i4i-instances-latest-intel-ice-lake): Up to 2.5x price/performance benefits and 5.3x speed up!
![2.5x relative price-performance improvement of i4i Photon](https://cms.databricks.com/sites/default/files/inline-images/db-325-blog-img-3.png)
- [Improved Performance and Value With Databricks Photon and Azure Lasv3 Instances Using AMD 3rd Gen EPYC™ 7763v Processors](https://www.databricks.com/blog/2022/10/11/improved-performance-and-value-databricks-photon-and-azure-lasv3-instances-using): Up to 2.5x price/performance benefits and 5.3x speed up!
- [Reduce Time to Decision With the Databricks Lakehouse Platform and Latest Intel 3rd Gen Xeon Scalable Processors](https://databricks.com/blog/2022/05/17/reduce-time-to-decision-with-the-databricks-lakehouse-platform-and-latest-intel-3rd-gen-xeon-scalable-processors.html):
"By enabling Databricks Photon and using Intel’s 3rd Gen Xeon Scalable processors, without making any code modifications, we were able to save ⅔ of the costs on our TPC-DS benchmark at 10TB and run 6.7 times quicker"
![price performance](https://databricks.com/wp-content/uploads/2022/05/db-165-blog-img-2.png)

#### Z-Ordering

- Delta Lake orders the data in the Parquet files to make range selection on object storage more efficient
- Limit the number of columns in the Z-Order to the best 1-4

#### ANALYZE

`ANALYZE TABLE db_name.table_name COMPUTE STATISTICS FOR ALL COLUMNS`

- Utilised for [Adaptive Query Execution](https://docs.databricks.com/spark/latest/spark-sql/aqe.html) (AQE), re-optimisations that occur during query execution
- 3 major features of AQE
  - Coalescing post-shuffle partitions (combine small partitions into reasonably sized partitions)
  - Converting sort-merge joins to broadcast hash joins
  - Skew join optimisation by splitting (and replicating if needed) skewed tasks into roughly evenly sized tasks
  - Dynamically detects and propagates empty relations
- `ANALYZE TABLE` collects table statistics that allows AQE to know which plan to choose for you

---

## Machine Learning (ML) & Artificial Intelligence (AI) 🧠

- [Selecting an Effective & Productive Machine Learning Platform](https://alexanderkwok17.medium.com/selecting-an-effective-productive-machine-learning-platform-8b7d7efa3d4f)

### MLOps

- [Architecting MLOps on the Lakehouse](https://databricks.com/blog/2022/06/22/architecting-mlops-on-the-lakehouse.html)
- [MLOps at Walgreens Boots Alliance With Databricks Lakehouse Platform](https://www.databricks.com/blog/2022/12/05/mlops-walgreens-boots-alliance-databricks-lakehouse-platform.html) - experiences with preview of MLOps Stack

### MLflow

- [▶️ MLflow YouTube channel](https://www.youtube.com/channel/UC5d6sLKbZahYMaAHgeYmoAg)
- [Cross-version Testing in MLflow](https://databricks.com/blog/2022/03/11/cross-version-testing-in-mlflow.html): MLflow integrates with several popular ML frameworks. See how the Databricks Engineering team proactively adapt MLflow and third-party libraries to prevent against breaking changes
- [Model Evaluation in MLflow](https://databricks.com/blog/2022/04/19/model-evaluation-in-mlflow.html)

### MLflow Recipes

- [A step-by-step guide to using MLFlow Recipes to refactor messy notebooks](https://fukumaruuu.medium.com/a-step-by-step-guide-to-using-mlflow-recipes-to-refactor-messy-notebooks-f78196b97ff0)

### Feature Store

- [eBook: The Comprehensive Guide to Feature Stores](https://databricks.com/wp-content/uploads/2022/03/The-Comprehensive-Guide-to-Feature-Stores.pdf) (Mar 2022)

### Distributed Training

- [How (Not) To Scale Deep Learning in 6 Easy Steps](https://www.databricks.com/blog/2019/08/15/how-not-to-scale-deep-learning-in-6-easy-steps.html)
- [Accelerating Your Deep Learning with PyTorch Lightning on Databricks](https://www.databricks.com/blog/2022/09/07/accelerating-your-deep-learning-pytorch-lightning-databricks.html)
- [Ray support on Databricks and Apache Spark Clusters](https://www.databricks.com/blog/2023/02/28/announcing-ray-support-databricks-and-apache-spark-clusters.html)
- [▶️ Scaling Deep Learning on Databricks](https://www.youtube.com/watch?v=A95_q24nA1o)
- [Rapid NLP Development With Databricks, Delta, and Transformers](https://www.databricks.com/blog/2022/09/09/rapid-nlp-development-databricks-delta-and-transformers.html)
- [Mitigating Bias in Machine Learning With SHAP and Fairlearn](https://www.databricks.com/blog/2022/09/16/mitigating-bias-machine-learning-shap-and-fairlearn.html)([accompanying 📄 notebook](https://www.databricks.com/wp-content/uploads/notebooks/db-336-mitigating_bias_with_shap_fairlearn-blog.html))
- [Parallel ML: How Compass Built a Framework for Training Many Machine Learning Models](https://www.databricks.com/blog/2022/07/20/parallel-ml-how-compass-built-a-framework-for-training-many-machine-learning-models-on-databricks.html)

### Predictions

- [Near Real-Time Anomaly Detection with Delta Live Tables and Databricks Machine Learning](https://www.databricks.com/blog/2022/08/08/near-real-time-anomaly-detection-with-delta-live-tables-and-databricks-machine-learning.html)

### Guides

- [Getting Started with Personalization through Propensity Scoring](https://databricks.com/blog/2022/06/03/getting-started-with-personalization-through-propensity-scoring.html) (accompanying [notebooks](https://d1r5llqwmkrl74.cloudfront.net/notebooks/nightly/RCG/Propensity/index.html#Propensity_1.html))
- [Building an End-to-End No Code Pipeline with Databricks](https://medium.com/@l.h.g/building-an-end-to-end-no-code-pipeline-with-databricks-18c3819dadf0)
- [Using MLflow to deploy Graph Neural Networks for Monitoring Supply Chain Risk](https://medium.com/@ajmal.t.aziz/using-mlflow-to-deploy-graph-neural-networks-for-monitoring-supply-chain-risk-644c87e5259e)
- [Predicting the 2022 World Cup with no-code data science and machine learning](https://medium.com/@andrewpweaver/predicting-the-2022-world-cup-with-no-code-data-science-and-machine-learning-134b459f4b1a): covers `bamboolib` + AutoML + serverless inference ([repo](https://github.com/andyweaves/worldcup22))
- [Fine-Tuning Large Language Models with Hugging Face and DeepSpeed](https://www.databricks.com/blog/2023/03/20/fine-tuning-large-language-models-hugging-face-and-deepspeed.html)
- [How Outreach Productionizes PyTorch-based Hugging Face Transformers for NLP](https://www.databricks.com/blog/2021/05/14/how-outreach-productionizes-pytorch-based-hugging-face-transformers-for-nlp.html)
- [Getting started with NLP using Hugging Face transformers pipelines](https://www.databricks.com/blog/2023/02/06/getting-started-nlp-using-hugging-face-transformers-pipelines.html)
- [Rapid NLP Development With Databricks, Delta, and Transformers](https://www.databricks.com/blog/2022/09/09/rapid-nlp-development-databricks-delta-and-transformers.html): Hugging Face, BERT
- [GPU-accelerated Sentiment Analysis Using Pytorch and Hugging Face on Databricks](https://www.databricks.com/blog/2021/10/28/gpu-accelerated-sentiment-analysis-using-pytorch-and-huggingface-on-databricks.html)
- [▶️ Streaming Data with Twitter, Delta Live Tables, Databricks Workflows, and Hugging Face](https://www.youtube.com/watch?v=LmHPk4jPnP8)
- [Quantifying uncertainty with Tensorflow Probability](https://databricks.com/blog/2022/04/28/how-wrong-is-your-model.html)
- [How Corning Built End-to-end ML on Databricks Lakehouse Platform](https://www.databricks.com/blog/2023/01/05/how-corning-built-end-end-ml-databricks-lakehouse-platform.html) ([▶️ AWS re:Invent 2022 talk](https://www.youtube.com/watch?v=DH_NQVT8Qc0))

---

## Geospatial 🌏

- [Mosaic](https://databrickslabs.github.io/mosaic/): a Databricks Labs extension to the Apache Spark framework that allows easy and fast processing of very large geospatial datasets
- [GitHub: Mosaic](https://github.com/databrickslabs/mosaic)
- [Building a Geospatial Lakehouse, Part 1](https://databricks.com/blog/2021/12/17/building-a-geospatial-lakehouse-part-1.html)
- [Building a Geospatial Lakehouse, Part 2](https://databricks.com/blog/2022/03/28/building-a-geospatial-lakehouse-part-2.html): includes downloadable notebooks
- [High Scale Geospatial Processing With Mosaic](https://databricks.com/blog/2022/05/02/high-scale-geospatial-processing-with-mosaic.html): writeup on the underlying philosophy behind Mosaic's design
- [Building Geospatial Data Products](https://www.databricks.com/blog/2023/01/06/building-geospatial-data-products.html)
- [Built-in H3 Expressions for Geospatial Processing and Analytics](https://www.databricks.com/blog/2022/09/14/announcing-built-h3-expressions-geospatial-processing-and-analytics.html)
- [Supercharging H3 for Geospatial Analytics](https://www.databricks.com/blog/2023/01/12/supercharging-h3-geospatial-analytics.html) _"In this blog, you will learn about the new expressions, performance benchmarks from our vectorized columnar implementation, and multiple approaches for point-in-polygon spatial joins using H3"_
- [Spatial Analytics at Any Scale With H3 and Photon: A Comparison of Discrete, Vector, and Hybrid Approaches](https://www.databricks.com/blog/2022/12/13/spatial-analytics-any-scale-h3-and-photon.html)
![Geospatial libraries decision tree](https://cms.databricks.com/sites/default/files/inline-images/db-400-blog-img-2.png)
- [How Thasos Optimized and Scaled Geospatial Workloads with Mosaic on Databricks](https://www.databricks.com/blog/2022/10/12/how-thasos-optimized-and-scaled-geospatial-workloads-mosaic-databricks.html): Thasos is an alternative data intelligence firm that transforms real-time location data from mobile phones into actionable business performance insights. To derive actionable insights from mobile phone ping data (a time series of points defined by a latitude and longitude pair), Thasos created, maintains and manages a vast collection of verified geofences
![Geofence polygons from Figure 1 showing contained H3 cells (in red) and the derived boundary chips (in blue)](https://cms.databricks.com/sites/default/files/inline-images/db-328-blog-img-2.jpg)
- [ArcGIS GeoAnalytics Engine in Databricks](https://www.databricks.com/blog/2022/12/07/arcgis-geoanalytics-engine-databricks.html)

---

## Use Cases

### App Dev

- [Taming JavaScript Exceptions With Databricks](https://databricks.com/blog/2022/01/25/taming-javascript-exceptions-with-databricks.html)

### Customer Data

- [Customer Entity Resolution](https://www.databricks.com/blog/2022/08/04/new-solution-accelerator-customer-entity-resolution.html) ([Solution Accelerator page](https://www.databricks.com/solutions/accelerators/customer-entity-resolution) | [Notebooks](https://d1r5llqwmkrl74.cloudfront.net/notebooks/nightly/RCG/Customer_ER/index.html))
- [The Emergence of the Composable Customer Data Platform](https://databricks.com/blog/2022/06/24/the-emergence-of-the-composable-customer-data-platform.html) ([whitepaper](https://cms.databricks.com/sites/default/files/2022-11/databricks_cdp_whitepaper_final-103122.pdf))

### Cybersecurity 🔐

- [Hunting for IOCs Without Knowing Table Names or Field Labels](https://databricks.com/blog/2022/07/15/hunting-for-iocs-without-knowing-table-names-or-field-labels.html)
- [Hunting Anomalous Connections and Infrastructure With TLS Certificates: TLS hashes as a source for the cybersecurity threat hunting program](https://databricks.com/blog/2022/01/20/hunting-anomalous-connections-and-infrastructure-with-tls-certificates.html)
- [Cybersecurity in the Era of Multiple Clouds and Regions](https://www.databricks.com/blog/2022/08/30/cybersecurity-era-multiple-clouds-and-regions.html)
- [Building ETL pipelines for the cybersecurity lakehouse with Delta Live Tables](https://databricks.com/blog/2022/06/03/building-etl-pipelines-for-the-cybersecurity-lakehouse-with-delta-live-tables.html): ingest & evaluate AWS CloudTrail & VPC Flow logs (accompanying notebooks: [CloudTrail DLT pipeline](https://databricks.com/wp-content/uploads/notebooks/db-172-dlt/cloudtrail-dlt-pipeline.html), [VPC Flow Logs DLT pipeline](https://databricks.com/wp-content/uploads/notebooks/db-172-dlt/vpc-flow-logs-dlt-pipeline.html), [Zeek DLT pipeline](https://databricks.com/wp-content/uploads/notebooks/db-172-dlt/zeek-dlt-pipeline.html))
- [Accelerating SIEM Migrations With the SPL to PySpark Transpiler](https://www.databricks.com/blog/2022/12/16/accelerating-siem-migrations-spl-pyspark-transpiler.html)
- [Learn how to connect Databricks to Okta to ingest System Logs, retain, and analyze for complete visibility using your Databricks Lakehouse Platform](https://databricks.com/blog/2022/04/07/analyzing-okta-logs-with-databricks-lakehouse-platform-to-detect-unusual-activity.html) (accompanying [notebooks](https://databricks.com/wp-content/uploads/notebooks/db-134-okta-logs/index.html#1_okta_create_table.html))
- [Streaming Windows Event Logs into the Cybersecurity Lakehouse](https://databricks.com/blog/2022/05/05/streaming-windows-event-logs-into-the-cybersecurity-lakehouse.html) ([notebook](https://github.com/DerekKing001/databricks_cyber_notebooks/blob/master/winlogbeats-kafka-sysmon/winlogbeats-kafka-sysmon-example.py))
- [Building a Cybersecurity Lakehouse for CrowdStrike Falcon Events Part I](https://databricks.com/blog/2021/05/20/building-a-cybersecurity-lakehouse-for-crowdstrike-falcon-events.html), [Part II](https://databricks.com/blog/2022/07/19/building-a-cybersecurity-lakehouse-for-crowdstrike-falcon-events-part-ii.html), [Part III](https://www.databricks.com/blog/2022/12/16/building-cybersecurity-lakehouse-crowdstrike-falcon-events-part-iii.html)
- [▶️ Vlogs on security engineering for big data and cybersecurity](https://www.youtube.com/@lipyeow-sec7733): by [Lipyeow Lim](https://www.linkedin.com/in/lipyeowlim/), Technical Director, Cybersecurity GTM, Databricks

### ERP

- [How Organizations Can Extract the Full Potential of SAP Data with a Lakehouse](https://www.databricks.com/blog/2022/09/20/how-organizations-can-extract-full-potential-sap-data-lakehouse.html)

### Marketing Analytics

- [How to Build a Marketing Analytics Solution Using Fivetran and dbt on the Databricks Lakehouse](https://www.databricks.com/blog/2022/08/03/how-to-build-a-marketing-analytics-solution-using-fivetran-and-dbt-on-the-databricks-lakehouse.html)

---

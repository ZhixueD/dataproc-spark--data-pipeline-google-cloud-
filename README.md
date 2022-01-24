# dataproc(spark) ETL data pipeline on google cloud platform
![resource](https://user-images.githubusercontent.com/98153604/150813213-cc08c8a6-c325-43a2-9f8a-40312891a7dc.png)


## Overview:

In this project, I have established a ETL data pipeline using dataproc(spark) on google cloud platform to extract data from google cloud storage (data lake), do some data transform and cleaning, and load data to Bigquery (data warehouse) for data analysis. The project includes a fully functioning pipeline of ingestion, ETL and data analysis and we will do it following these steps:

1. Create Google Cloud Storage Bucket
2. Create a virtual machine from google compute engine, using virtual machine to download data from Kaggle open datasets and upload it google cloud storage
3. Create a python file for Dataproc and PySpark
4. Create a workflow
5. Data analyze in Bigquery and tableau

## 1 — Create Google Cloud Storage Bucket




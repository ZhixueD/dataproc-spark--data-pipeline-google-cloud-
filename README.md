# dataproc(spark) ETL data pipeline on google cloud platform
![resource](https://user-images.githubusercontent.com/98153604/150813213-cc08c8a6-c325-43a2-9f8a-40312891a7dc.png)


## Overview:

About datasets:

This dataset is a subset of Yelp's businesses, reviews, and user data. The dataset include information about businesses across 8 metropolitan areas in the USA and Canada. This dataset contains five JSON files and the user agreement. In this project we will focus on two JSON files: yelp_academic_dataset_business.json, yelp_academic_dataset_review.json.
The Api for this datasets is:'kaggle datasets download -d yelp-dataset/yelp-dataset'.


In this project, I have established a ETL data pipeline using dataproc(spark) on google cloud platform to extract data from google cloud storage (data lake), do some data transform and cleaning, and load data to Bigquery (data warehouse) for data analysis. The project includes a fully functioning pipeline of ingestion, ETL and data analysis and we will do it following these steps:

1. Create Google Cloud Storage Bucket
2. Create a virtual machine from google compute engine.
3. using virtual machine to install packages and download data from Kaggle open datasets and upload it google cloud storage.
4. Create a dataproc cluster
5. Create a python file for Dataproc and PySpark
6. Create a workflow
7. Data analyze in Bigquery (by using Bigquery ML for creating a machine learing model of recommendation system for restaurant for user).
8. Tableau for data visulization and analyze

## 1. Create Google Cloud Storage Bucket

 Create a bucket for storage raw dataset download from kaggle.
 
 ![google cloud storage](https://user-images.githubusercontent.com/98153604/150821254-d17296a9-09f5-4723-850a-543084ff2169.JPG)

## 2. Create a virtual machine from google compute engine

In google console, select compute engine. In compute engine, create a vm instance.

![vm2](https://user-images.githubusercontent.com/98153604/150822993-a29fa59d-ee49-4d0b-add0-e8d1325479e6.JPG)

## 3. Using virtual machine to install packages and download data from Kaggle open datasets and upload it to google cloud storage.

Click SSH in your VM machine

![vm for download](https://user-images.githubusercontent.com/98153604/150823949-830990b2-a4e3-432c-8d8b-34ca42bda483.JPG)

### RUN Some code to install some package first:

#### sudo apt-get install python3-pip

#### sudo pip3 pip install pyspark

### using kaggle API to download data into VM Machine (code not show)

### copy datasets from VM Machine to google cloud storage

#### gsutil cp *.json gs://t-osprey-337221/t-osprey-337221-yelp

![yelp datasets in GCS](https://user-images.githubusercontent.com/98153604/150826698-55a024e1-d3b1-42b9-ac06-631e97c7987f.JPG)

## 4. Create a dataproc cluster follow next steps, this will also allowd run spark Pipeline using Google jupyter nootbook:

(1) Configure and start a Cloud Dataproc cluster

(2) In the GCP Console, on the Navigation menu, in the Big Data section, click Dataproc.

(3) Click Create Cluster.

(4) Enter the Cluster Name.

(5) In the Versioning section, click Change and select 2.0 (Debian 10, Hadoop 3.2, Spark 3.1).

(6) Click Select.

(7) In the Components > Component gateway section, select Enable component gateway.

(8) Under Optional components, Select Jupyter Notebook.

(9) Click Create.

after dataproc cluster has create, a staging folder and a temp folder in Google cloud storage will also be estabilish, copy jupyter file which you create to nookbook/jupyter folder.

![staging folder](https://user-images.githubusercontent.com/98153604/150829972-19e5952d-5a13-4650-8c33-e272fee4c142.JPG)

Click Web Interfaces in dataproc cluster, and here you can ran jupyter file which you establish (in the attachment), but here I choose to directly run python file which I writen to create in a dataproc job for ETL pipeline.

## 5. Create a python file for Dataproc and PySpark （python file in attachment) and save the file to google cloud storage

![pycode](https://user-images.githubusercontent.com/98153604/150832104-c4d2da68-993c-4bfd-bb5b-b95863aa1c18.JPG)

## 6. Create a workflow

in the VM machine run code, and will start a dataproc job: 
![submit dataproc job](https://user-images.githubusercontent.com/98153604/150832944-42551f5e-3552-40c6-9e71-abae871ee1a4.JPG)

## 7. Data analyze in Bigquery (by using Bigquery ML for creating a machine learing model of recommendation system for restaurant for user).

After dataproc (spark) ETL pipeline, the data after cleaning and transforming has successfully saved in Bigquery. Bigquery is a data warehouse held by google cloud.

![bigquery data](https://user-images.githubusercontent.com/98153604/150865380-b026272d-77f2-4e78-91ef-c9ae8f354583.JPG)

![bigquery data2](https://user-images.githubusercontent.com/98153604/150865592-572842cc-e408-4676-ae72-5de1a1467447.JPG)

Since bigquery support machine learing analysis directly in bigquery, by using Bigquery ML, here I plan to create a recommendation machine learning model for user of Yelp company to recommend restaurant. This is a classic recommmendation system, which I will use matrix_factorization machine learning model type to tranning my data.
To trainning the data is easy, I just need to run a SQL query in Bigquery:

![machine learning SQL](https://user-images.githubusercontent.com/98153604/150866940-21d48a62-87f8-408b-a054-94dadeacbad6.JPG)

However, I did not proceed the machine learning because the machine learing need large compute resourses provide by google. And my google account do not have the right to order these resourses. 

## 8. Tableau for data visulization and analysis

By using Tableau to connect Bigquery, I do some data visulization and analyze by using Tableau

























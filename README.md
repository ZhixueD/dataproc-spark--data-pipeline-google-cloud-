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
4. Create a python file for Dataproc and PySpark
5. Create a workflow
6. Data analyze in Bigquery (by using Bigquery ML for creating a machine learing model of recommendation system for restaurant for user).

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















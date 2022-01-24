"""
Migrating data from Google cloud storage(Data lake) to BigQuery(Data warehouse) via Dataproc (Apache Spark) -- ETL.
The raw data from kaggle(kaggle datasets download -d yelp-dataset/yelp-dataset) has already download to Google cloud storage (data lake) via VM engine (google cloud). The data are json files. In Spark, these can be read using spark.read.json()
"""

from pyspark.sql import SparkSession, SQLContext, Row

#gcs_bucket
gcs_bucket='t-osprey-337221-yelp'

#initial spark
spark = SparkSession.builder.appName("yelp").getOrCreate()
sc = spark.sparkContext

# Read data from gcs_bucket
business = "gs://"+gcs_bucket+"//.yelp-dataset/yelp_academic_dataset_business.json"
review ="gs://"+gcs_bucket+"//.yelp-dataset/yelp_academic_dataset_review.json"
business_df = spark.read.json(business)
review_df = spark.read.json(review)
print('business table schema')
business_df.printSchema()
print('review table schema')
review_df.printSchema()

# create temp table for SparkSQL
business_df.createOrReplaceTempView("business_table")
review_df.createOrReplaceTempView("review_table")




# only select restaurant and is open from business table, and do some column selection
restaurant_df = spark.sql("""
                            select 
                            business_id, name, city, latitude, longitude, review_count, stars, state, address
                            from 
                            business_table
                            where categories like '%Restaurants%'and is_open=1
                            """)

# create temp table for SparkSQL
restaurant_df.createOrReplaceTempView("restaurant_table")

print('total number from restaurant table')
restaurant_df.count()
spark.sql("""
            select count(*) from restaurant_table""").show()

#check if business_id has duplicate
spark.sql("""
            select count(business_id) as num from restaurant_table group by business_id having num >1""").show()

#check if business_id and stars has Null value
spark.sql("""
            select * from restaurant_table where business_id IS NULL or stars is null""").show(5)




#Column selection from review table, and stars column is not null, user_id is not null
review_df = spark.sql("""
                        select review_id, business_id, user_id, cool, date, funny, stars as review_stars, useful
                        from 
                        review_table
                        where stars is not null and review_id is not null and user_id is not null and business_id is not null""")
review_df.show(5)
review_df.createOrReplaceTempView("review_edit_table")

#check if review_id has duplicate
spark.sql("""
            select count(review_id) from review_edit_table group by review_id having count(review_id)>1""").show()
print('total number from review table')
spark.sql("""
            select count(*) from review_edit_table""").show()

#caculate total review number and average stars for each business_id
spark.sql("""
            select business_id, count(business_id) as num, avg(review_stars) from review_edit_table 
            group by business_id order by num desc""").cache().show(10)





#Merge business table and review together, using right join
yelp_restaurant = spark.sql(""" select 
          restaurant.*, review_id, user_id, cool, date, funny, review_stars, useful
          from 
          restaurant_table restaurant 
          inner join review_edit_table rt 
          on restaurant.business_id = rt.business_id"""
         )
yelp_restaurant.printSchema()
yelp_restaurant.count()




#save yelp_restaurant table to bigquery
yelp_restaurant.write.mode('overwrite').format('bigquery') \
  .option("temporaryGcsBucket", "dataproc-temp-europe-north1-306478473038-3r6aj13k") \
  .option('table', 'yelp.yelp_restaurant2') \
  .save()
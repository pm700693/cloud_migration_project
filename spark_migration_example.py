# Sample Spark job optimized for GCP Dataproc
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('migrate').getOrCreate()
df = spark.read.parquet('/mnt/hdfs/export/')
df.write.parquet('gs://your-bucket/processed/')

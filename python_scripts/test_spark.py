from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("RetailPipeline") \
    .getOrCreate()

df = spark.read.csv(
    "datasets/raw/olist_orders_dataset.csv",
    header=True,
    inferSchema=True
)

df.show(5)

spark.stop()
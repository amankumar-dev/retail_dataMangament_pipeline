import os
from pyspark.sql import SparkSession
from dotenv import load_dotenv

load_dotenv('.env')

USER=os.getenv('DB_USER')
PASSWORD=os.getenv('DB_PASSWORD')
HOST=os.getenv('DB_HOST')
PORT=os.getenv('DB_PORT')
NAME=os.getenv('DB_NAME')
DB_URL=f'jdbc:postgresql://{HOST}:{PORT}/{NAME}'

spark=SparkSession.builder.appName('connection').config(
        "spark.jars.packages",
        "org.postgresql:postgresql:42.7.3"
    ).getOrCreate()

def read_table(tableName):
    return(
        spark.read \
            .format('jdbc') \
            .option('url',DB_URL) \
            .option('dbtable',tableName) \
            .option('user',USER) \
            .option('password',PASSWORD) \
            .option('driver','org.postgresql.Driver') \
            .load()
    )
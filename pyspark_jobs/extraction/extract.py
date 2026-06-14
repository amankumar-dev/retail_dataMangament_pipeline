from pyspark.sql import SparkSession
from pyspark.sql.functions import when,col,trim,lower,count,filter,round,expr,unix_timestamp
from pyspark.sql.types import StringType
import numpy as np
import uuid
spark=SparkSession.builder.appName('temp').getOrCreate()

cust=spark.read.csv(r'/mnt/d/aman/aman.code/dataengproject/retail_management/datasets/raw/customers.csv',
                    inferSchema=True,
                    header=True)

geo=spark.read.csv(r'/mnt/d/aman/aman.code/dataengproject/retail_management/datasets/raw/geolocation.csv',
                   inferSchema=True,
                   header=True)

orddetails=spark.read.csv(r'/mnt/d/aman/aman.code/dataengproject/retail_management/datasets/raw/orderDetails.csv',
                     inferSchema=True,
                     header=True)

orders=spark.read.csv(r'/mnt/d/aman/aman.code/dataengproject/retail_management/datasets/raw/orders.csv',
                      inferSchema=True,
                      header=True)

payment=spark.read.csv(r'/mnt/d/aman/aman.code/dataengproject/retail_management/datasets/raw/payment.csv',
                       inferSchema=True,
                       header=True)

prodName=spark.read.csv(r'/mnt/d/aman/aman.code/dataengproject/retail_management/datasets/raw/productNameEng.csv',
                        inferSchema=True,
                        header=True)

prod=spark.read.csv(r'/mnt/d/aman/aman.code/dataengproject/retail_management/datasets/raw/products.csv',
                    inferSchema=True,
                    header=True)

review=spark.read.csv(r'/mnt/d/aman/aman.code/dataengproject/retail_management/datasets/raw/reviews.csv',
                      inferSchema=True,
                      header=True)

seller=spark.read.csv(r'/mnt/d/aman/aman.code/dataengproject/retail_management/datasets/raw/sellers.csv',
                      inferSchema=True,
                      header=True)



print(payment.filter(
    col('payment_type').isNull()
).count())
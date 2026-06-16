from pyspark.sql.functions import when,col,trim,lower,count,filter,round,expr,unix_timestamp
from pyspark.sql.types import StringType
import numpy as np
import uuid
from pyspark_jobs.db_connection.py_db import read_table

cust=read_table('silver.customers')

geo=read_table('silver.geolocation')

orddetails=read_table('bronze.orddetails')

orders=read_table('silver.orders')

payment=read_table('silver.payment')

prodName=read_table('silver.prodeng')

prod=read_table('silver.prod')

review=read_table('silver.reviews')

seller=read_table('silver.sellers')


orddetails.show()
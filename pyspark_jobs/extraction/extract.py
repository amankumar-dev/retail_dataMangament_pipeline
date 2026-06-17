from pyspark.sql.functions import when,col,trim,lower,count,filter,round,expr,unix_timestamp
from pyspark.sql.types import StringType
import numpy as np
import uuid
from pyspark_jobs.db_connection.py_db import read_table

cust=read_table('bronze.customers')

geo=read_table('bronze.geolocation')

orddetails=read_table('bronze.orddetails')

orders=read_table('bronze.orders')

payment=read_table('bronze.payment')

prodName=read_table('bronze.prodeng')

prod=read_table('bronze.prod')

review=read_table('bronze.reviews')

seller=read_table('bronze.sellers')


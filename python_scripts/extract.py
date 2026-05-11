# Store csv into dataframe

import pandas as pd

customers=pd.read_csv('datasets/raw/customers.csv')
geolocation=pd.read_csv('datasets/raw/geolocation.csv')
orderItems=pd.read_csv('datasets/raw/orderDetails.csv')
orders=pd.read_csv('datasets/raw/orders.csv')
payment=pd.read_csv('datasets/raw/payment.csv')
productName=pd.read_csv('datasets/raw/products.csv')
reviews=pd.read_csv('datasets/raw/reviews.csv')
sellers=pd.read_csv('datasets/raw/sellers.csv')
product=pd.read_csv('datasets/raw/products.csv')

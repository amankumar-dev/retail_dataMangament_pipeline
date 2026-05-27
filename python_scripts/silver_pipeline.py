from python_scripts.extract_bronze import extract_bronze_data
from sql.load_silver import insert_silver_customer,insert_silver_geolocation,insert_silver_orddetails,insert_silver_sellers,insert_silver_prodEng,insert_silver_prod,insert_silver_orders
from python_scripts.silver_transform import customers_data,geolocation_data,orderDetails_data,orders_data,seller_data,review_data,prod_data,prodName_data,payment_data
import numpy as np

# Fetching data from bronze schema
#customers=extract_bronze_data('customers')
#geolocation=extract_bronze_data('geolocation')
orddetails=extract_bronze_data('orddetails')
#orders=extract_bronze_data('orders')
#payment=extract_bronze_data('payment')
#prodEng=extract_bronze_data('prodEng')
#products=extract_bronze_data('prod')
#reviews=extract_bronze_data('reviews')
#sellers=extract_bronze_data('sellers')

# Df transformation
#customers=customers_data(customers)
#geolocation=geolocation_data(geolocation)
orddetails=orderDetails_data(orddetails)
#sellers=seller_data(sellers)
#prodEng=prodName_data(prodEng)
#products=prod_data(products)
#orders=orders_data(orders)

# Load data in silver schema
#insert_silver_customer(customers,'customers')
#insert_silver_geolocation(geolocation,'geolocation')
#insert_silver_sellers(sellers,'sellers')
#insert_silver_prodEng(prodEng,'prodEng')
#insert_silver_prod(products,'prod')
#insert_silver_orders(orders,'orders')
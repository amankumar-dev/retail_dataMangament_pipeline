from python_scripts.extract import customers,geolocation,orderDetails,orders,payment,product,productName,reviews,sellers
from python_scripts.metadata import ingestion
from sql.load_bronze import insert_bronze_customer,insert_bronze_geolocation,insert_bronze_orderDetails,insert_bronze_orders,insert_bronze_payment,insert_bronze_prodEng,insert_bronze_prod,insert_bronze_reviews,insert_bronze_sellers
import uuid

# Creating batch Id
batch_id = str(uuid.uuid4())

# Using ingestion to add metadata
customers=ingestion(customers,'customer.csv',batch_id)
geolocation=ingestion(geolocation,'geolocation.csv',batch_id)
orders=ingestion(orders,'orders.csv',batch_id)
orderDetails=ingestion(orderDetails,'orderDetails.csv',batch_id)
payment=ingestion(payment,'payment.csv',batch_id)
productName=ingestion(productName,'productName.csv',batch_id)
product=ingestion(product,'product.csv',batch_id)
reviews=ingestion(reviews,'reviews.csv',batch_id)
sellers=ingestion(sellers,'sellers.csv',batch_id)

# Inserting value into bronze schema
#insert_bronze_customer(customers,'customers')
#insert_bronze_geolocation(geolocation,'geolocation')
#insert_bronze_orderDetails(orderDetails,'orddetails')
#insert_bronze_orders(orders,'orders')
#insert_bronze_payment(payment,'payment')
#insert_bronze_prodEng(productName,'prodeng')
#insert_bronze_prod(product,'prod')
#insert_bronze_reviews(reviews,'reviews')
insert_bronze_sellers(sellers,'sellers')
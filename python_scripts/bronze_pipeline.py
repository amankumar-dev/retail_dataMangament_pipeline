from extract import customers,geolocation,orderItems,orders,payment,product,productName,reviews,sellers
from metadata import ingestion
import uuid

# Creating batch Id
batch_id = str(uuid.uuid4())

# Using ingestion to add metadata
customers=ingestion(customers,'customer.csv',batch_id)
geolocation=ingestion(geolocation,'geolocation.csv',batch_id)
orders=ingestion(orders,'orders.csv',batch_id)
orderItems=ingestion(orderItems,'orderDetails.csv',batch_id)
payment=ingestion(payment,'payment.csv',batch_id)
productName=ingestion(productName,'productName.csv',batch_id)
product=ingestion(product,'product.csv',batch_id)
reviews=ingestion(reviews,'reviews.csv',batch_id)
sellers=ingestion(sellers,'sellers.csv',batch_id)

print(customers.info())
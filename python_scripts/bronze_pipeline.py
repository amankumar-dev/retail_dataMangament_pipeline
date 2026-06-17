from python_scripts.extract import customers,geolocation,orderDetails,orders,payment,product,productName,reviews,sellers
from python_scripts.metadata import ingestion
from sql.load_bronze import insert_bronze_customer,insert_bronze_geolocation,insert_bronze_orderDetails,insert_bronze_orders,insert_bronze_payment,insert_bronze_prodEng,insert_bronze_prod,insert_bronze_reviews,insert_bronze_sellers
import uuid

# Creating batch Id
batch_id = str(uuid.uuid4())

# Creating datasets to make code clean
datasets=[
    (customers,'customer.csv',insert_bronze_customer,'customers'),
    (geolocation,'geolocation.csv',insert_bronze_geolocation,'geolocation'),
    (orderDetails,'orderDetails.csv',insert_bronze_orderDetails,'orddetails'),
    (orders,'orders.csv',insert_bronze_orders,'orders'),
    (payment,'payment.csv',insert_bronze_payment,'payment'),
    (productName,'productNameEng.csv',insert_bronze_prodEng,'prodeng'),
    (product,'products.csv',insert_bronze_prod,'prod'),
    (reviews,'reviews.csv',insert_bronze_reviews,'reviews'),
    (sellers,'sellers.csv',insert_bronze_sellers,'sellers')
]

#print(orderDetails.head(5))

for df,source,load_fun,table in datasets:
    df=ingestion(df,source,batch_id)
    df.to_csv(f'/mnt/d/aman/aman.code/dataengproject/retail_management/datasets/bronze/bronze_{source}',index=False)
    load_fun(df,table)
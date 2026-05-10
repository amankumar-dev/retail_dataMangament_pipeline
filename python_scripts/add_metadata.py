import pandas as pd
import uuid
from export_csvData import customers,geolocation,orders,orderItems,payment,productName,product,reviews,sellers

batch_id = str(uuid.uuid4())

def ingestion(df,source):
    # Adding metadata 
    df['timestamp']=pd.Timestamp.now()
    df['source']=source
    df['batch_id']=batch_id
    
    return df

customers=ingestion(customers,'customer.csv')
geolocation=ingestion(geolocation,'geolocation.csv')
orders=ingestion(orders,'orders.csv')
orderItems=ingestion(orderItems,'orderItems.csv')
payment=ingestion(payment,'payment.csv')
productName=ingestion(productName,'productName.csv')
product=ingestion(product,'product.csv')
reviews=ingestion(reviews,'reviews.csv')
sellers=ingestion(sellers,'sellers.csv')


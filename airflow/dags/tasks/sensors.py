from airflow.sdk import task
from airflow.sdk.bases.sensor import PokeReturnValue
import os
import logging

log=logging.getLogger(__name__)

required_files=[
    'customers.csv',
    'geolocation.csv',
    'orderDetails.csv',
    'orders.csv',
    'payment.csv',
    'productNameEng.csv',
    'products.csv',
    'reviews.csv',
    'sellers.csv'
]

BASE_PATH='/mnt/d/Aman/aman.code/dataengproject/retail_management/datasets/raw'

@task.sensor(poke_interval=30,timeout=600)
def wait_bronze():
    missing_files=[]
    for file in required_files:
        path=os.path.join(BASE_PATH,file)
        if not os.path.exists(path):
            missing_files.append(file)
    
    if missing_files:
        log.warning(f"Missing File: {missing_files}")
        return PokeReturnValue(
            is_done=False,
            xcom_value=missing_files
        )
    else:
        return PokeReturnValue(
            is_done=True,
            xcom_value=required_files
        )
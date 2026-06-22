# Extracting data from bronze schema table for silver utilization

from sql.connection import conn
import pandas as pd

def extract_bronze_data(tableName):
    try:
        query=f'SELECT * FROM bronze.{tableName};'
        df=pd.read_sql(query,conn)
        return df
    except Exception as e:
        print(f'{tableName} data not fetched ',e)
        return None
    
    
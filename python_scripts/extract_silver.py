# Extracting data from silver schema table for gold utilization

from sql.connection import conn
import pandas as pd

def extract_silver_data(tableName):
    try:
        query=f'SELECT * FROM silver.{tableName};'
        df=pd.read_sql(query,conn)
        #print(f'{tableName} bronze data fetched successfully')
        return df
    except Exception as e:
        print(f'{tableName} data not fetched ',e)
        return None
    
    
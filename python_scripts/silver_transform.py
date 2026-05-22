# For transforming the raw data
import pandas as pd
import numpy as np
from python_scripts.silver_pipeline import customers,geolocation,orddetails
import uuid

# For customers transformation
def customers_data(df):
    columns=df.columns
    for cols in columns:
        # Convert string NaN into numpy NaN    
       df[f'{cols}']=df[f'{cols}'].replace('NaN',np.nan)
       
       # Standarize text
       if cols not in ['cust_zipcode','timestampp']:
           df[f'{cols}']=df[f'{cols}'].str.lower().str.strip()
    
    #Handle null for customer unique id
    mask=df['cust_unq_id'].isna()
    df.loc[mask,'cust_unq_id']=[str(uuid.uuid4()) for _ in range(mask.sum())]
    
    #Handle null for customer id
    df['cust_id']=df['cust_id'].fillna('NA')
    
    # Fix datatypes
    df['cust_zipcode']=df['cust_zipcode'].astype(str).str.strip()
    
    # Drop full empty row
    df=df.dropna(how='all')
    
    return df

# For geolocation transformation
def geolocation_data(df):
    columns=df.columns
    
    # Convert string NaN into numpy NaN
    for cols in columns:
        # Convert string NaN into numpy NaN    
        df[f'{cols}']=df[f'{cols}'].replace('NaN',np.nan)
       
       # Standarize text
        if cols not in ['timestampp']:
            df[f'{cols}']=df[f'{cols}'].astype(str)
            df[f'{cols}']=df[f'{cols}'].str.lower().str.strip()
            
    # Handle null value
    df[['geo_city','geo_state']]=df[['geo_city','geo_state']].fillna('NA')

# For order details transformation
def orderDetails_data(df):
    pass
# For transforming the raw data
import pandas as pd
import numpy as np
import uuid

# For customers transformation
def customers_data(df):
    # Convert string NaN into numpy NaN    
    df = df.replace(r'^\s*(nan|na)?\s*$',
        np.nan,
        regex=True
    )    
    
    columns=df.columns
    
    for cols in columns:
       # Standarize text
       if cols not in ['cust_zipcode', 'timestampp']:

            mask = df[cols].notna()

            df.loc[mask, cols] = (
                df.loc[mask, cols]
                .str.lower()
                .str.strip()
            )
    
    #Handle null for customer unique id
    mask=df['cust_unq_id'].isna()
    df.loc[mask,'cust_unq_id']=[str(uuid.uuid4()) for _ in range(mask.sum())]
    
    # Fix datatypes
    df['cust_zipcode']=df['cust_zipcode'].astype(str).str.strip()
    
    # Drop full empty row
    df=df.dropna(how='all')
    
    # Drop duplcated value
    df=df.drop_duplicates()
    df=df.drop_duplicates(subset=['cust_unq_id'])
    
    return df

# For geolocation transformation
def geolocation_data(df):
    # Convert string NaN into numpy NaN           
    df = df.replace(r'^\s*(nan|na)?\s*$',
        np.nan,
        regex=True
    )   
    
    columns=df.columns
    
    # Convert string NaN into numpy NaN
    for cols in columns:
       # Standarize text
        if cols not in ['timestampp']:
            df[f'{cols}']=df[f'{cols}'].astype(str)
            df[f'{cols}']=df[f'{cols}'].str.lower().str.strip()
            
    # Handle null value
    df[['geo_city','geo_state']]=df[['geo_city','geo_state']].fillna('NA')
    
    # Standarize value
    df['geo_lat'] = df['geo_lat'].round(4)
    df['geo_lng'] = df['geo_lng'].round(4)
    
    # Drop duplcated value
    df=df.drop_duplicates()
    df=df.drop_duplicates(subset=['geo_zipcode','geo_lat','geo_lng'])
    
    return df

# For order details transformation
def orderDetails_data(df):
    columns=df.columns
    
    # Convert string nan into numpy nan
    for cols in columns:
        df[f'{cols}']=df[f'{cols}'].replace('NaN',np.nan)
        # Standarize value
        if(pd.api.types.is_string_dtype(df[f'{cols}'])):
            df[f'{cols}']=df[f'{cols}'].str.lower().str.strip()
        
    # Handle null
    df['order_id']=df['order_id'].fillna('NA')
    df['prod_id']=df['prod_id'].fillna('NA')
    
    # Drop duplcated value
    df=df.drop_duplicates()
    
    return df
     
# For order transformation
def orders_data(df):
    columns=df.columns
    
    # Convert string nan into numpy nan
    for cols in columns:
        df[f'{cols}']=df[f'{cols}'].replace('NaN',np.nan)
        # Standarize value
        if(pd.api.types.is_string_dtype(df[f'{cols}'])):
            df[f'{cols}']=df[f'{cols}'].str.lower().str.strip()
            
    # Hanle nulls
    df['order_id']=df['order_id'].fillna('NA')
    df['cust_id']=df['cust_id'].fillna('NA')
    approved_mask=df['approved_at'].isna()
    df.loc[approved_mask,'approved_at']=(df.loc[approved_mask,'purchase_timestamp']+pd.Timedelta(minutes=15))
    carrier_mask=df['delivered_carrier_date'].isna()
    df.loc[carrier_mask,'delivered_carrier_date']=(df.loc[carrier_mask,'approved_at']+pd.Timedelta(days=2))
    delivery_mask=df['delivered_customer_date'].isna()
    df.loc[delivery_mask,'delivered_customer_date']=(df.loc[delivery_mask,'delivered_carrier_date']+pd.Timedelta(days=4))
    
    # Business rule implementation
    mask=(df['approved_at']>df['delivered_carrier_date'])
    df.loc[mask,'delivered_carrier_date']=(df.loc[mask,'approved_at']+pd.Timedelta(days=2))
    mask=(df['delivered_carrier_date']>df['delivered_customer_date'])
    df.loc[mask,'delivered_customer_date']=(df.loc[mask,'delivered_carrier_date']+pd.Timedelta(days=2))
    
    # Handle wrong status value availability
    shipMask=(df['ord_status']=='shipped')
    df.loc[shipMask,'delivered_customer_date']=pd.NaT
    canMask=(df['ord_status']=='canceled')
    df.loc[canMask,'delivered_customer_date']=pd.NaT
    df.loc[canMask,'estimated_delivery_date']=pd.NaT
    invMask=(df['ord_status']=='invoiced')
    df.loc[invMask,'delivered_customer_date']=pd.NaT
    df.loc[invMask,'delivered_carrier_date']=pd.NaT
    df.loc[invMask,'estimated_delivery_date']=pd.NaT
    
    # Drop duplcated value
    df=df.drop_duplicates()
    
    return df
    
# For payment transformation
def payment_data(df):
    columns=df.columns

    # Convert string nan into numpy nan
    for cols in columns:
        df[f'{cols}']=df[f'{cols}'].replace('NaN',np.nan)
        # Standarize value
        if(pd.api.types.is_string_dtype(df[f'{cols}'])):
            df[f'{cols}']=df[f'{cols}'].str.lower().str.strip()
    
    # Handling null value
    df['payment_type']=df['payment_type'].fillna('voucher')
    
    # Drop duplcated value
    df=df.drop_duplicates()
    
    return df

# For product name transformation
def prodName_data(df):
    columns=df.columns
    
    # Convert string nan into numpy nan
    for cols in columns:
        df[f'{cols}']=df[f'{cols}'].replace('NaN',np.nan)
        # Standarize value
        if(pd.api.types.is_string_dtype(df[f'{cols}'])):
            df[f'{cols}']=df[f'{cols}'].fillna('NA').str.lower().str.strip()
            
    # Drop duplcated value
    df=df.drop_duplicates()
    
    return df

# For product transformation
def prod_data(df):
    columns=df.columns
    
    # Convert string nan into numpy nan
    for cols in columns:
        df[f'{cols}']=df[f'{cols}'].replace('NaN',np.nan)
        # Standarize value
        if(pd.api.types.is_string_dtype(df[f'{cols}'])):
            df[f'{cols}']=df[f'{cols}'].str.lower().str.strip()
    
    # Drop duplcated value
    df=df.drop_duplicates()
    
    return df

# For review transformation
def review_data(df):
    columns=df.columns
    
    # Convert string nan into numpy nan
    for cols in columns:
        df[f'{cols}']=df[f'{cols}'].replace('NaN',np.nan)
        # Standarize value
        if(pd.api.types.is_string_dtype(df[f'{cols}'])):
            df[f'{cols}']=df[f'{cols}'].fillna('NA').str.lower().str.strip()
            
    # Drop duplcated value
    df=df.drop_duplicates()
    
    return df
  
# For seller transformation
def seller_data(df):
    columns=df.columns
    
    # Convert string nan into numpy nan
    for cols in columns:
        df[f'{cols}']=df[f'{cols}'].replace('NaN',np.nan)
        # Standarize value
        if(pd.api.types.is_string_dtype(df[f'{cols}'])):
            df[f'{cols}']=df[f'{cols}'].fillna('NA').str.lower().str.strip()
    
    # Drop duplcated value
    df=df.drop_duplicates()
    
    return df



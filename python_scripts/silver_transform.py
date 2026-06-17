# For transforming the raw data
import pandas as pd
import numpy as np
import uuid
from sql.connection import conn

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
    df=df.drop_duplicates(subset=['cust_id'])
    
    return df

# For geolocation transformation
def geolocation_data(df):
    # Convert string NaN into numpy NaN           
    df = df.replace(r'^\s*(nan|na)?\s*$',
        np.nan,
        regex=True
    )   
    
    columns=df.columns
    
    # Standarize value
    df['geo_lat'] = df['geo_lat'].round(4)
    df['geo_lng'] = df['geo_lng'].round(4)
    
    # Convert string NaN into numpy NaN
    for cols in columns:
       # Standarize text
        if cols not in ['timestampp']:
            df[f'{cols}']=df[f'{cols}'].astype(str)
            df[f'{cols}']=df[f'{cols}'].str.lower().str.strip()
    
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
    
    # For order_sk mapping
    ord_df=pd.read_sql('''SELECT order_id,order_sk
                            FROM silver.orders;''',conn)
    
    # For prod_sk mapping
    prod_df=pd.read_sql('''SELECT prod_id,prod_sk
                            FROM silver.prod;''',conn)
    
    # For seller_sk mapping
    seller_df=pd.read_sql('''SELECT seller_id,seller_sk
                                FROM silver.sellers;''',conn)
    
    ord_df = ord_df.dropna(subset=['order_id']).drop_duplicates(subset=['order_id'])
    prod_df = prod_df.dropna(subset=['prod_id']).drop_duplicates(subset=['prod_id'])
    seller_df = seller_df.dropna(subset=['seller_id']).drop_duplicates(subset=['seller_id'])
    
    df=df.merge(
        ord_df,
        how='left',
        on='order_id'
    )
    
    df=df.merge(
        prod_df,
        on='prod_id',
        how='left'
    )
    
    df=df.merge(
        seller_df,
        on='seller_id',
        how='left'
    )
    
    df['order_sk'] = df['order_sk'].astype('Int64')
    df['prod_sk'] = df['prod_sk'].astype('Int64')
    df['seller_sk'] = df['seller_sk'].astype('Int64')
    
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
    
    # Handle null    
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
    df=df.dropna(subset=['order_id']).drop_duplicates(subset=['order_id'])
    
    # cust_sk mapping
    cust_df = pd.read_sql(
        '''
        SELECT cust_id, cust_sk
        FROM silver.customers
        ''',
        conn
    )
    df = df.merge(
        cust_df,
        on='cust_id',
        how='left'
    )
    
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
    
    # For order_sk mapping
    ord_df=pd.read_sql('''SELECT order_id,order_sk
                            FROM silver.orders;''',conn)
    
    ord_df = ord_df.dropna(subset=['order_id']).drop_duplicates(subset=['order_id'])    
    
    df=df.merge(
        ord_df,
        how='left',
        on='order_id'
    )
    
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
            df[f'{cols}']=df[f'{cols}'].str.lower().str.strip()
            
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
    df = df.drop_duplicates(subset=['prod_id'])
    return df

# For review transformation
def review_data(df):
    columns=df.columns
    
    # Convert string nan into numpy nan
    for cols in columns:
        df[f'{cols}']=df[f'{cols}'].replace('NaN',np.nan)
        # Standarize value
        if(pd.api.types.is_string_dtype(df[f'{cols}'])):
            df[f'{cols}']=df[f'{cols}'].str.lower().str.strip()

    # Handle duplicates
    mask=df['review_id'].duplicated()
    df.loc[mask,'review_id']=None
    
    # For order_sk mapping
    ord_df=pd.read_sql('''SELECT order_id,order_sk
                            FROM silver.orders;''',conn)
    
    ord_df = ord_df.dropna(subset=['order_id']).drop_duplicates(subset=['order_id'])
    
    df=df.merge(
        ord_df,
        how='left',
        on='order_id'
    )
    
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
            df[f'{cols}']=df[f'{cols}'].str.lower().str.strip()
    
    # Drop duplcated value
    df=df.drop_duplicates()
    df = df.drop_duplicates(subset=['seller_id'])
    return df

def debug_orddetails_merge():
    raw_df = pd.read_sql(
        "SELECT * FROM bronze.orddetails",
        conn
    )

    print("\n===== INITIAL =====")
    print("Raw:", raw_df.shape)

    ord_df = pd.read_sql(
        "SELECT order_id, order_sk FROM silver.orders",
        conn
    )

    print("\n===== ORDERS =====")
    print("orders shape:", ord_df.shape)
    print("duplicate order_id:", ord_df['order_id'].duplicated().sum())
    print("null order_id:", ord_df['order_id'].isna().sum())

    temp = raw_df.merge(
        ord_df,
        on='order_id',
        how='left'
    )

    print("After order merge:", temp.shape)

    prod_df = pd.read_sql(
        "SELECT prod_id, prod_sk FROM silver.prod",
        conn
    )

    print("\n===== PRODUCTS =====")
    print("prod shape:", prod_df.shape)
    print("duplicate prod_id:", prod_df['prod_id'].duplicated().sum())
    print("null prod_id:", prod_df['prod_id'].isna().sum())

    temp = temp.merge(
        prod_df,
        on='prod_id',
        how='left'
    )

    print("After product merge:", temp.shape)

    seller_df = pd.read_sql(
        "SELECT seller_id, seller_sk FROM silver.sellers",
        conn
    )

    print("\n===== SELLERS =====")
    print("seller shape:", seller_df.shape)
    print("duplicate seller_id:", seller_df['seller_id'].duplicated().sum())
    print("null seller_id:", seller_df['seller_id'].isna().sum())

    temp = temp.merge(
        seller_df,
        on='seller_id',
        how='left'
    )

    print("After seller merge:", temp.shape)

    print("\n===== FINAL =====")
    print("duplicates rows:", temp.duplicated().sum())
    print("final shape:", temp.shape)


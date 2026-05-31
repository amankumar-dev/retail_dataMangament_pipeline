import pandas as pd
from python_scripts.extract_silver import extract_silver_data
from sql.connection import conn

df=extract_silver_data('orddetails')
#print(df.head(5))

# For sellers table
def transform_sellers(df):
    df=df[['seller_sk','seller_id','seller_zipcode','seller_city','seller_state']]
    return df

# For customer table
def transform_cust(df):
    df=df[['cust_sk','cust_id','cust_city','cust_state']]
    return df
    
# For prodeng table
def transform_prodeng(df):
    df=df[['prod_name_id','prod_cat_name','prod_cat_name_eng']]
    return df

# For prod table
def transform_prod(df):
    df=df[['prod_sk','prod_id','prod_cat_name','prod_name_len','prod_desc_len','prod_photos_qty','prod_weight_g','prod_length_cm','prod_height_cm','prod_width_cm']]
    return df

# For date table
def transform_date(df):
    start_date = df['purchase_timestamp'].min()
    end_date = df['purchase_timestamp'].max()

    dates = pd.date_range(
        start=start_date,
        end=end_date,
        freq='D'
    )

    date_df = pd.DataFrame({
        'full_date': dates
    })

    date_df['day'] = date_df['full_date'].dt.day
    date_df['month'] = date_df['full_date'].dt.month
    date_df['year'] = date_df['full_date'].dt.year
    date_df['quarter'] = date_df['full_date'].dt.quarter

    date_df['day_name'] = date_df['full_date'].dt.day_name()
    date_df['month_name'] = date_df['full_date'].dt.month_name()

    date_df['week_of_year'] = date_df['full_date'].dt.isocalendar().week

    date_df['is_weekend'] = date_df['full_date'].dt.dayofweek >= 5

    # Optional: convert datetime to date
    date_df['full_date'] = date_df['full_date'].dt.date

    return date_df

# For location table
def transform_location(df):
    df=df[['geo_id','geo_zipcode','geo_lat','geo_lng','geo_city','geo_state']]
    return df

# For fact table
def transform_fact(df):
    df=df[['order_id','prod_sk','seller_sk']]
    ord_df=pd.read_sql('''SELECT
                            od.order_id,
                            od.prod_sk,
                            od.seller_sk,
                            o.cust_sk
                            FROM silver.orddetails od
                            LEFT JOIN silver.orders o
                        ON od.order_id = o.order_id;''',conn)
    print(ord_df.head(5))
    
transform_fact(df)
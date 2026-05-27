from sql.connection import conn,cursor
import pandas as pd

# For removing old data
def truncate_silver_data(tableName):
    with conn:
        try:
            cursor.execute(f'TRUNCATE TABLE silver.{tableName} RESTART IDENTITY CASCADE;')
            print(f'{tableName} Old data removed')
            return True
        except Exception as e:
            print(f'{tableName} Old data not removed ',e)
            return False

# For dynamic columns
def dynamic_cols(df):
    columns=df.columns.tolist()     # Convert column name into list of col
    col_name=','.join(columns)      # Convert list of col into single string
    placeholders=','.join(['%s']*len(columns))        # Creating string of placeholders with same size of columns
    df = df.astype(object).where(pd.notnull(df), None)                # Convert nan into none
    data = list(df.itertuples(index=False, name=None))      # Converting df row into list of tuple
    return [col_name,placeholders,data]

# Insert into silver table
# For customer
def insert_silver_customer(df,tableName):
    if(truncate_silver_data(tableName)):
        with conn:
            try:
                result=dynamic_cols(df)
                query=f'INSERT INTO silver.{tableName}({result[0]}) VALUES({result[1]});'     # Creating dynamic query
                data=result[2]
                cursor.executemany(query,data)      # Executing multiple query
                print(f'{tableName} data inserted')
            except Exception as e:
                print(f'{tableName} data not inserted ',e)

# For Geolocation
def insert_silver_geolocation(df,tableName):
    if(truncate_silver_data(tableName)):
        with conn:
            try:
                result=dynamic_cols(df)
                query=f'INSERT INTO silver.{tableName}({result[0]}) VALUES({result[1]});'
                data=result[2]
                cursor.executemany(query,data)
                print(f'{tableName} data inserted')
            except Exception as e:
                print(f'{tableName} data not inserted ',e)
                
#For orddetails
def insert_silver_orddetails(df,tableName):
    if(truncate_silver_data(tableName)):
        with conn:
            try:
                result=dynamic_cols(df)
                query=f'INSERT INTO silver.{tableName}({result[0]}) VALUES({result[1]});'
                data=result[2]
                cursor.executemany(query,data)
                print(f'{tableName} data inserted')
            except Exception as e:
                print(f'{tableName} data not inserted ',e)
                
# For sellers
def insert_silver_sellers(df,tableName):
    if(truncate_silver_data(tableName)):
        with conn:
            try:
                result=dynamic_cols(df)
                query=f'INSERT INTO silver.{tableName}({result[0]}) VALUES({result[1]});'
                data=result[2]
                cursor.executemany(query,data)
                print(f'{tableName} data inserted')
            except Exception as e:
                print(f'{tableName} data not inserted ',e)
                
# For prodEng
def insert_silver_prodEng(df,tableName):
    if(truncate_silver_data(tableName)):
        with conn:
            try:
                result=dynamic_cols(df)
                query=f'INSERT INTO silver.{tableName}({result[0]}) VALUES({result[1]});'
                data=result[2]
                cursor.executemany(query,data)
                print(f'{tableName} data inserted')
            except Exception as e:
                print(f'{tableName} data not inserted ',e)
                
# For prod
def insert_silver_prod(df,tableName):
    if(truncate_silver_data(tableName)):
        with conn:
            try:
                result=dynamic_cols(df)
                query=f'INSERT INTO silver.{tableName}({result[0]}) VALUES({result[1]});'
                data=result[2]
                cursor.executemany(query,data)
                print(f'{tableName} data inserted')
            except Exception as e:
                print(f'{tableName} data not inserted ',e)
                
# For orders
def insert_silver_orders(df,tableName):
    if(truncate_silver_data(tableName)):
        with conn:
            try:
                result=dynamic_cols(df)
                query=f'INSERT INTO silver.{tableName}({result[0]}) VALUES({result[1]});'
                data=result[2]
                cursor.executemany(query,data)
                print(f'{tableName} data inserted')
            except Exception as e:
                 print(f'{tableName} data not inserted ',e)

from sql.connection import conn,cursor
from psycopg2.extras import execute_values
import pandas as pd

# For removing old data
def truncate_gold_data(tableName):
    with conn:
        try:
            cursor.execute(f'TRUNCATE TABLE gold.{tableName} RESTART IDENTITY CASCADE;')
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

def insert_dim_customer(tableName,df):
    if(truncate_gold_data(tableName)):
        with conn:
            try:
                result=dynamic_cols(df)
                query=f'INSERT INTO gold.{tableName}({result[0]}) VALUES({result[1]});'     # Creating dynamic query
                data=result[2]
                cursor.executemany(query,data)      # Executing multiple query
                print(f'{tableName} data inserted')
            except Exception as e:
                print(f'{tableName} data not inserted ',e)
                
def insert_dim_date(tableName,df):
    if(truncate_gold_data(tableName)):
        with conn:
            try:
                result=dynamic_cols(df)
                query=f'INSERT INTO gold.{tableName}({result[0]}) VALUES({result[1]});'     # Creating dynamic query
                data=result[2]
                cursor.executemany(query,data)      # Executing multiple query
                print(f'{tableName} data inserted')
            except Exception as e:
                print(f'{tableName} data not inserted ',e)

def insert_dim_location(tableName,df):
    if(truncate_gold_data(tableName)):
        with conn:
            try:
                result=dynamic_cols(df)
                query=f'INSERT INTO gold.{tableName}({result[0]}) VALUES({result[1]});'     # Creating dynamic query
                data=result[2]
                cursor.executemany(query,data)      # Executing multiple query
                print(f'{tableName} data inserted')
            except Exception as e:
                print(f'{tableName} data not inserted ',e)
                
def insert_dim_prod(tableName,df):
    if(truncate_gold_data(tableName)):
        with conn:
            try:
                result=dynamic_cols(df)
                query=f'INSERT INTO gold.{tableName}({result[0]}) VALUES({result[1]});'     # Creating dynamic query
                data=result[2]
                cursor.executemany(query,data)      # Executing multiple query
                print(f'{tableName} data inserted')
            except Exception as e:
                print(f'{tableName} data not inserted ',e)
                
def insert_dim_prodeng(tableName,df):
    if(truncate_gold_data(tableName)):
        with conn:
            try:
                result=dynamic_cols(df)
                query=f'INSERT INTO gold.{tableName}({result[0]}) VALUES({result[1]});'     # Creating dynamic query
                data=result[2]
                cursor.executemany(query,data)      # Executing multiple query
                print(f'{tableName} data inserted')
            except Exception as e:
                print(f'{tableName} data not inserted ',e)

def insert_dim_seller(tableName,df):
    if(truncate_gold_data(tableName)):
        with conn:
            try:
                result=dynamic_cols(df)
                query=f'INSERT INTO gold.{tableName}({result[0]}) VALUES({result[1]});'     # Creating dynamic query
                data=result[2]
                cursor.executemany(query,data)      # Executing multiple query
                print(f'{tableName} data inserted')
            except Exception as e:
                print(f'{tableName} data not inserted ',e)

def insert_fact_sales(tableName,df):
    if(truncate_gold_data(tableName)):
        with conn:
            try:
                result=dynamic_cols(df)
                query=f'INSERT INTO gold.{tableName}({result[0]}) VALUES({result[1]});'     # Creating dynamic query
                data=result[2]
                cursor.executemany(query,data)      # Executing multiple query
                print(f'{tableName} data inserted')
            except Exception as e:
                print(f'{tableName} data not inserted ',e)
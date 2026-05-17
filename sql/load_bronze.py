# Here we will insert all the data into bronze table
from sql.connection import conn,cursor

# Insert into bronze tables
# For removing old data
def truncate_bronze_data(tableName):
    with conn:
        try:
            cursor.execute(f'TRUNCATE TABLE bronze.{tableName} CASCADE;')
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
    data=[tuple(row) for row in df.to_numpy()]      # Converting df row into list of tuple
    return [col_name,placeholders,data]

# For customer
def insert_bronze_customer(df,tableName):
    if(truncate_bronze_data(tableName)):
        with conn:
            try:
                result=dynamic_cols(df)
                query=f'INSERT INTO bronze.{tableName}({result[0]}) VALUES({result[1]});'     # Creating dynamic query
                data=result[2]
                cursor.executemany(query,data)      # Executing multiple query
                print(f'{tableName} data inserted')
            except Exception as e:
                print(f'{tableName} data not inserted ',e)
                
def insert_bronze_geolocation(df,tableName):
    if(truncate_bronze_data(f'{tableName}')):
        with conn:
            try:
                result=dynamic_cols(df)
                query=f'INSERT INTO bronze.{tableName}({result[0]}) VALUES({result[1]});'     # Creating dynamic query
                data=result[2]
                cursor.executemany(query,data)      # Executing multiple query
                print(f'{tableName} data inserted')
            except Exception as e:
                print(f'{tableName} data not inserted ',e)
                
def insert_bronze_orderDetails(df,tableName):
    if(truncate_bronze_data(f'{tableName}')):
        with conn:
            try:
                result=dynamic_cols(df)
                query=f'INSERT INTO bronze.{tableName}({result[0]}) VALUES({result[1]});'     # Creating dynamic query
                data=result[2]
                cursor.executemany(query,data)      # Executing multiple query
                print(f'{tableName} data inserted')
            except Exception as e:
                print(f'{tableName} data not inserted ',e)
                
def insert_bronze_orders(df,tableName):
    if(truncate_bronze_data(f'{tableName}')):
        with conn:
            try:
                result=dynamic_cols(df)
                query=f'INSERT INTO bronze.{tableName}({result[0]}) VALUES({result[1]});'     # Creating dynamic query
                data=result[2]
                cursor.executemany(query,data)      # Executing multiple query
                print(f'{tableName} data inserted')
            except Exception as e:
                print(f'{tableName} data not inserted ',e)
                
def insert_bronze_payment(df,tableName):
    if(truncate_bronze_data(f'{tableName}')):
        with conn:
            try:
                result=dynamic_cols(df)
                query=f'INSERT INTO bronze.{tableName}({result[0]}) VALUES({result[1]});'     # Creating dynamic query
                data=result[2]
                cursor.executemany(query,data)      # Executing multiple query
                print(f'{tableName} data inserted')
            except Exception as e:
                print(f'{tableName} data not inserted ',e)
                
def insert_bronze_prodEng(df,tableName):
    if(truncate_bronze_data(f'{tableName}')):
        with conn:
            try:
                result=dynamic_cols(df)
                query=f'INSERT INTO bronze.{tableName}({result[0]}) VALUES({result[1]});'     # Creating dynamic query
                data=result[2]
                cursor.executemany(query,data)      # Executing multiple query
                print(f'{tableName} data inserted')
            except Exception as e:
                print(f'{tableName} data not inserted ',e)
                
def insert_bronze_prod(df,tableName):
    if(truncate_bronze_data(f'{tableName}')):
        with conn:
            try:
                result=dynamic_cols(df)
                query=f'INSERT INTO bronze.{tableName}({result[0]}) VALUES({result[1]});'     # Creating dynamic query
                data=result[2]
                cursor.executemany(query,data)      # Executing multiple query
                print(f'{tableName} data inserted')
            except Exception as e:
                print(f'{tableName} data not inserted ',e)
                
def insert_bronze_reviews(df,tableName):
    if(truncate_bronze_data(f'{tableName}')):
        with conn:
            try:
                result=dynamic_cols(df)
                query=f'INSERT INTO bronze.{tableName}({result[0]}) VALUES({result[1]});'     # Creating dynamic query
                data=result[2]
                cursor.executemany(query,data)      # Executing multiple query
                print(f'{tableName} data inserted')
            except Exception as e:
                print(f'{tableName} data not inserted ',e)
                
def insert_bronze_sellers(df,tableName):
    if(truncate_bronze_data(f'{tableName}')):
        with conn:
            try:
                result=dynamic_cols(df)
                query=f'INSERT INTO bronze.{tableName}({result[0]}) VALUES({result[1]});'     # Creating dynamic query
                data=result[2]
                cursor.executemany(query,data)      # Executing multiple query
                print(f'{tableName} data inserted')
            except Exception as e:
                print(f'{tableName} data not inserted ',e)
                


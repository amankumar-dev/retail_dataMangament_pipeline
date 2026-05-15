# Here we will insert all the data into bronze table
from connection import conn,cursor

# Insert into bronze tables
# For removing old data
def truncate_bronze_data(tableName):
    with conn:
        try:
            cursor.execute(f'TRUNCATE TABLE bronze.{tableName};')
            print(f'{tableName} Old data removed')
            return True
        except Exception as e:
            print(f'{tableName} Old data not removed ',e)
            return False

# For customer
def insert_bronze_customer(df):
    if(truncate_bronze_data('customers')):
        with conn:
            try:
                query='''INSERT INTO bronze.customers(
                                    cust_id,
                                    cust_unq_id,
                                    cust_zipcode,
                                    cust_city,
                                    cust_state,
                                    cust_name,
                                    cust_timestamp,
                                    source,
                                    batch_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);'''
                data=[]
                for _,row in df.iterrows():
                    data.append((row['customer_id'],
                                row['customer_unique_id'],
                                row['customer_zip_code_prefix'],
                                row['customer_city'],
                                row['customer_state'],
                                row['customer_name'],
                                row['timestamp'],
                                row['source'],
                                row['batch_id']))
                cursor.executemany(query,data)
                print('customer data inserted')
            except Exception as e:
                print('customer data not inserted ',e)
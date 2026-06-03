from sql.connection import conn,cursor

def create_gold_schema():
    with conn:
        try:
            cursor.execute('''CREATE SCHEMA IF NOT EXISTS gold;''')
            print('gold schema created')
        except Exception as e:
            print('gold schema not created ',e)

def create_dim_customer(tableName):
    with conn:
        try:
            cursor.execute(f'''CREATE TABLE IF NOT EXISTS gold.{tableName}(
                                cust_sk INT PRIMARY KEY,
                                cust_id VARCHAR(255),
                                cust_city VARCHAR(255),
                                cust_state VARCHAR(255));''')
            print(f'{tableName} got created')
        except Exception as e:
            print(f'{tableName} not created ',e)

def create_dim_location(tableName):
    with conn:
        try:
            cursor.execute(f'''CREATE TABLE IF NOT EXISTS gold.{tableName}(
                                geo_id INT PRIMARY KEY,
                                geo_zipcode INT,
                                geo_lat DOUBLE PRECISION,
                                geo_lng DOUBLE PRECISION,
                                geo_city VARCHAR(255),
                                geo_state VARCHAR(255));''')
            print(f'{tableName} got created')
        except Exception as e:
            print(f'{tableName} not created ',e)
            
def create_dim_prod(tableName):
    with conn:
        try:
            cursor.execute(f'''CREATE TABLE IF NOT EXISTS gold.{tableName}(
                                prod_sk SERIAL PRIMARY KEY,
                                prod_id VARCHAR(255),
                                prod_cat_name VARCHAR(255) REFERENCES gold.dim_prodeng(prod_cat_name) ON DELETE CASCADE ON UPDATE CASCADE,
                                prod_name_len NUMERIC(10,2),
                                prod_desc_len NUMERIC(10,2),
                                prod_photos_qty NUMERIC(10,2),
                                prod_weight_g NUMERIC(10,2),
                                prod_length_cm NUMERIC(10,2),
                                prod_height_cm NUMERIC(10,2),
                                prod_width_cm NUMERIC(10,2));''')
            print(f'{tableName} got created')
        except Exception as e:
            print(f'{tableName} not created ',e)
            
def create_dim_prodeng(tableName):
    with conn:
        try:
            cursor.execute(f'''CREATE TABLE IF NOT EXISTS gold.{tableName}(
                                prod_name_id INT PRIMARY KEY,
                                prod_cat_name VARCHAR(255) UNIQUE,
                                prod_cat_name_eng VARCHAR(255));''')
            print(f'{tableName} got created')
        except Exception as e:
            print(f'{tableName} not created ',e)

def create_dim_sellers(tableName):
    with conn:
        try:
            cursor.execute(f'''CREATE TABLE IF NOT EXISTS gold.{tableName}(
                                seller_sk SERIAL PRIMARY KEY,
                                seller_id VARCHAR(255),
                                seller_zipcode INT,
                                seller_city VARCHAR(255),
                                seller_state VARCHAR(255));''')
            print(f'{tableName} got created')
        except Exception as e:
            print(f'{tableName} not created ',e)

def create_dim_date(tableName):
    with conn:
        try:
            cursor.execute(f'''CREATE TABLE IF NOT EXISTS gold.{tableName}(
                                date_sk SERIAL PRIMARY KEY,
                                full_date DATE UNIQUE,
                                day INT,
                                month INT,
                                year INT,
                                quarter INT,
                                day_name VARCHAR(20),
                                month_name VARCHAR(20),
                                week_of_year INT,
                                is_weekend BOOLEAN);''')
            print(f'{tableName} got created')
        except Exception as e:
            print(f'{tableName} not created ',e)

def create_fact_sales(tableName):
    with conn:
        try:
            cursor.execute(f'''CREATE TABLE IF NOT EXISTS gold.{tableName}(
                                sales_sk SERIAL PRIMARY KEY,
                                cust_sk INT REFERENCES gold.dim_cust(cust_sk) ON DELETE CASCADE ON UPDATE CASCADE,
                                prod_sk INT REFERENCES gold.dim_prod(prod_sk) ON DELETE CASCADE ON UPDATE CASCADE,
                                seller_sk INT REFERENCES gold.dim_seller(seller_sk) ON DELETE CASCADE ON UPDATE CASCADE,
                                date_sk INT REFERENCES gold.dim_date(date_sk) ON DELETE CASCADE ON UPDATE CASCADE,
                                order_sk INT,
                                order_id VARCHAR(255),
                                ord_status VARCHAR(30),
                                payment_type VARCHAR(50),
                                payment_installments INT,
                                price NUMERIC(10,2),
                                freight_val NUMERIC(10,2),
                                payment_val NUMERIC(10,2),
                                rev_score INT);''')
            print(f'{tableName} got created')
        except Exception as e:
            print(f'{tableName} not created ',e)
            
create_gold_schema()
create_dim_sellers('dim_seller')
create_dim_customer('dim_cust')
create_dim_prodeng('dim_prodeng')
create_dim_prod('dim_prod')
create_dim_date('dim_date')
create_dim_location('dim_location')
create_fact_sales('fact_sales')
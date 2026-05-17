from connection import conn,cursor

# Create bronze schema
def create_bronze_schema():
    with conn:
        try:
            cursor.execute('''CREATE SCHEMA IF NOT EXISTS bronze
                           ''')
            print('bronze schema created')
        except Exception as e:
            print(e)

# Create bronze tables
# Customer table
def bronze_table_customer():
    with conn:
        try:
            cursor.execute('''CREATE TABLE IF NOT EXISTS bronze.customers(
                            cust_id VARCHAR(255),
                            cust_unq_id VARCHAR(255),
                            cust_zipcode INT,
                            cust_city VARCHAR(255),
                            cust_state VARCHAR(255),
                            cust_name VARCHAR(255),
                            timestampp TIMESTAMPTZ,
                            source VARCHAR(255),
                            batch_id VARCHAR(255));''')
            print('bronze customer table created')
        except Exception as e:
            print('customer table not created ',e)

# Geolocation table
def bronze_table_geolocation():
    with conn:
        try:
            cursor.execute('''CREATE TABLE IF NOT EXISTS bronze.geolocation(
                                geo_zipcode INT,
                                geo_lat DOUBLE PRECISION,
                                geo_lng DOUBLE PRECISION,
                                geo_city VARCHAR(255),
                                geo_state VARCHAR(255),
                                timestampp TIMESTAMPTZ,
                                source VARCHAR(255),
                                batch_id VARCHAR(255))''')
            print('bronze geolocation table created')
        except Exception as e:
            print('bronze geolocation table not created ',e)
           
# Orders table
def bronze_table_orders():
    with conn:
        try:
            cursor.execute('''CREATE TABLE IF NOT EXISTS bronze.orders(
                                order_id VARCHAR(255) ,
                                cust_id VARCHAR(255) ,
                                ord_status VARCHAR(30),
                                purchase_timestamp TIMESTAMP,
                                approved_at TIMESTAMP,
                                delivered_carrier_date TIMESTAMP,
                                delivered_customer_date TIMESTAMP,
                                estimated_delivery_date TIMESTAMP,
                                timestampp TIMESTAMP,
                                source VARCHAR(255),
                                batch_id VARCHAR(255));''')
            print('bronze order table created')
        except Exception as e:
            print('order table not created ',e)        

# OrderDetails table
def bronze_table_orderdetails():
    with conn:
        try:
            cursor.execute('''CREATE TABLE IF NOT EXISTS bronze.orddetails(
                                order_id VARCHAR(255),
                                order_item_id INT,
                                prod_id VARCHAR(255),
                                seller_id VARCHAR(255),
                                shipp_limit_date TIMESTAMP,
                                price DOUBLE PRECISION,
                                freight_val DOUBLE PRECISION,
                                timestampp TIMESTAMP,
                                source VARCHAR(255),
                                batch_id VARCHAR(255));''')
            print('orderdetails table got created')
        except Exception as e:
            print('orderdetails not created ',e)

# Payment table
def bronze_table_payment():
    with conn:
        try:
            cursor.execute('''CREATE TABLE IF NOT EXISTS bronze.payment(
                                order_id VARCHAR(255),
                                payment_seq INT,
                                payment_type VARCHAR(50),
                                payment_installments INT,
                                payment_value DOUBLE PRECISION,
                                timestampp TIMESTAMP,
                                source VARCHAR(255),
                                batch_id VARCHAR(255));''')
            print('payment table created')
        except Exception as e:
            print('payment table not created ',e)

# Product Name in English table
def bronze_table_prodEng():
    with conn:
        try:
            cursor.execute('''CREATE TABLE IF NOT EXISTS bronze.prodEng(
                                prod_cat_name VARCHAR(255) ,
                                prod_cat_name_eng VARCHAR(255),
                                timestampp TIMESTAMP,
                                source VARCHAR(255),
                                batch_id VARCHAR(255))''')
            print('product name table created')
        except Exception as e:
            print('product name table not created ',e)
            
# Products table
def bronze_table_prod():
    with conn:
        try:
            cursor.execute('''CREATE TABLE IF NOT EXISTS bronze.prod(
                                prod_id VARCHAR(255) ,
                                prod_cat_name VARCHAR(255),
                                prod_name_len DOUBLE PRECISION,
                                prod_desc_len DOUBLE PRECISION,
                                prod_photos_qty DOUBLE PRECISION,
                                prod_weight_g DOUBLE PRECISION,
                                prod_length_cm DOUBLE PRECISION,
                                prod_height_cm DOUBLE PRECISION,
                                prod_width_cm DOUBLE PRECISION,
                                timestampp TIMESTAMP,
                                source VARCHAR(255),
                                batch_id VARCHAR(255))''')
            print('prod table created')
        except Exception as e:
            print('prod table not created ',e)
            
# Reviews Table
def bronze_table_reviews():
    with conn:
        try:
            cursor.execute('''CREATE TABLE IF NOT EXISTS bronze.reviews(
                                review_id VARCHAR(255) ,
                                order_id VARCHAR(255) ,
                                rev_score INT,
                                rev_comment_title VARCHAR(255),
                                rev_comment_message TEXT,
                                rev_creation_date TIMESTAMP,
                                rev_answer_timestamp TIMESTAMP,
                                timestampp TIMESTAMP,
                                source VARCHAR(255),
                                batch_id VARCHAR(255))''')
            print('review table created')
        except Exception as e:
            print('review table not created ',e)

# Sellers Table
def bronze_table_sellers():
    with conn:
        try:
            cursor.execute('''CREATE TABLE IF NOT EXISTS bronze.sellers(
                                seller_id VARCHAR(255) ,
                                seller_zipcode INT,
                                seller_city VARCHAR(255),
                                seller_state VARCHAR(255),
                                timestampp TIMESTAMP,
                                source VARCHAR(255),
                                batch_id VARCHAR(255))''')
            print('sellers table created')
        except Exception as e:
            print('sellers table not created ',e)


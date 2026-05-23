from sql.connection import conn,cursor

# Creating silver schema
def create_silver_schema():
    with conn:
        try:
            cursor.execute('CREATE SCHEMA IF NOT EXISTS silver;')
            print('silver schema created')
        except Exception as e:
            print('silver scheam not created')
            
# Create silver tables
# Customer table
def silver_table_customer():
    with conn:
        try:
            cursor.execute('''CREATE TABLE IF NOT EXISTS silver.customers(
                            cust_sk SERIAL PRIMARY KEY,
                            cust_id VARCHAR(255),
                            cust_unq_id UUID UNIQUE,
                            cust_zipcode INT,
                            cust_city VARCHAR(255),
                            cust_state VARCHAR(255),
                            cust_name VARCHAR(255),
                            timestampp TIMESTAMPTZ,
                            source VARCHAR(255),
                            batch_id UUID);''')
            print('silver customer table created')
        except Exception as e:
            print('customer table not created ',e)

# Geolocation table
def silver_table_geolocation():
    with conn:
        try:
            cursor.execute('''CREATE TABLE IF NOT EXISTS silver.geolocation(
                                geo_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                                geo_zipcode INT,
                                geo_lat DOUBLE PRECISION,
                                geo_lng DOUBLE PRECISION,
                                geo_city VARCHAR(255),
                                geo_state VARCHAR(255),
                                timestampp TIMESTAMPTZ,
                                source VARCHAR(255),
                                batch_id UUID,
                                UNIQUE(geo_zipcode, geo_lat, geo_lng))''')
            print('silver geolocation table created')
        except Exception as e:
            print('silver geolocation table not created ',e)
      
# Orders table
def silver_table_orders():
    with conn:
        try:
            cursor.execute('''CREATE TABLE IF NOT EXISTS silver.orders(
                                order_sk SERIAL PRIMARY KEY,
                                order_id VARCHAR(255),
                                cust_sk INT REFERENCES silver.customers(cust_sk) ON DELETE CASCADE ON UPDATE CASCADE,
                                cust_id VARCHAR(255),
                                ord_status VARCHAR(30),
                                purchase_timestamp TIMESTAMP,
                                approved_at TIMESTAMP,
                                delivered_carrier_date TIMESTAMP,
                                delivered_customer_date TIMESTAMP,
                                estimated_delivery_date TIMESTAMP,
                                timestampp TIMESTAMP,
                                source VARCHAR(255),
                                batch_id UUID);''')
            print('silver order table created')
        except Exception as e:
            print('order table not created ',e)        

# OrderDetails table
def silver_table_orderdetails():
    with conn:
        try:
            cursor.execute('''CREATE TABLE IF NOT EXISTS silver.orddetails(
                                orddetail_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                                order_sk INT REFERENCES silver.orders(order_sk) ON DELETE CASCADE ON UPDATE CASCADE,
                                order_id VARCHAR(255),
                                order_item_id INT,
                                prod_sk INT REFERENCES silver.prod(prod_sk) ON DELETE CASCADE ON UPDATE CASCADE,
                                prod_id VARCHAR(255),
                                seller_sk INT REFERENCES silver.sellers(seller_sk) ON DELETE CASCADE ON UPDATE CASCADE,
                                seller_id VARCHAR(255),
                                shipp_limit_date TIMESTAMP,
                                price NUMERIC(10,2),
                                freight_val NUMERIC(10,2),
                                timestampp TIMESTAMP,
                                source VARCHAR(255),
                                batch_id UUID);''')
            print('orderdetails table got created')
        except Exception as e:
            print('orderdetails not created ',e)

# Payment table
def silver_table_payment():
    with conn:
        try:
            cursor.execute('''CREATE TABLE IF NOT EXISTS silver.payment(
                                payment_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                                order_sk INT REFERENCES silver.orders(order_sk) ON DELETE CASCADE ON UPDATE CASCADE,
                                order_id VARCHAR(255)
                                payment_seq INT,
                                payment_type VARCHAR(50),
                                payment_installments INT,
                                payment_value NUMERIC(10,2),
                                timestampp TIMESTAMP,
                                source VARCHAR(255),
                                batch_id UUID);''')
            print('payment table created')
        except Exception as e:
            print('payment table not created ',e)

# Product Name in English table
def silver_table_prodEng():
    with conn:
        try:
            cursor.execute('''CREATE TABLE IF NOT EXISTS silver.prodEng(
                                prod_name_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                                prod_cat_name VARCHAR(255) UNIQUE,
                                prod_cat_name_eng VARCHAR(255),
                                timestampp TIMESTAMP,
                                source VARCHAR(255),
                                batch_id UUID)''')
            print('product name table created')
        except Exception as e:
            print('product name table not created ',e)

# Products table
def silver_table_prod():
    with conn:
        try:
            cursor.execute('''CREATE TABLE IF NOT EXISTS silver.prod(
                                prod_sk SERIAL PRIMARY KEY,
                                prod_id VARCHAR(255,
                                prod_cat_name VARCHAR(255) REFERENCES silver.prodeng(prod_cat_name) ON DELETE CASCADE ON UPDATE CASCADE,
                                prod_name_len NUMERIC(10,2),
                                prod_desc_len NUMERIC(10,2),
                                prod_photos_qty NUMERIC(10,2),
                                prod_weight_g NUMERIC(10,2),
                                prod_length_cm NUMERIC(10,2),
                                prod_height_cm NUMERIC(10,2),
                                prod_width_cm NUMERIC(10,2),
                                timestampp TIMESTAMP,
                                source VARCHAR(255),
                                batch_id UUID)''')
            print('prod table created')
        except Exception as e:
            print('prod table not created ',e)

# Reviews Table
def silver_table_reviews():
    with conn:
        try:
            cursor.execute('''CREATE TABLE IF NOT EXISTS silver.reviews(
                                review_id VARCHAR(255) PRIMARY KEY,
                                order_id VARCHAR(255) REFERENCES silver.orders(order_id) ON DELETE CASCADE ON UPDATE CASCADE,
                                rev_score INT,
                                rev_comment_title VARCHAR(255),
                                rev_comment_message TEXT,
                                rev_creation_date TIMESTAMP,
                                rev_answer_timestamp TIMESTAMP,
                                timestampp TIMESTAMP,
                                source VARCHAR(255),
                                batch_id UUID)''')
            print('review table created')
        except Exception as e:
            print('review table not created ',e)

# Sellers Table
def silver_table_sellers():
    with conn:
        try:
            cursor.execute('''CREATE TABLE IF NOT EXISTS silver.sellers(
                                seller_id VARCHAR(255) PRIMARY KEY,
                                seller_zipcode INT,
                                seller_city VARCHAR(255),
                                seller_state VARCHAR(255),
                                timestampp TIMESTAMP,
                                source VARCHAR(255),
                                batch_id UUID)''')
            print('sellers table created')
        except Exception as e:
            print('sellers table not created ',e)

create_silver_schema()
silver_table_customer()
silver_table_sellers()
silver_table_prodEng()
silver_table_prod()
silver_table_geolocation()
silver_table_orders()
silver_table_orderdetails()
silver_table_payment()
silver_table_reviews()
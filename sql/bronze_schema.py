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
            cursor.execute('''CREATE TABLE IF NOT EXISTS customers(
                            cust_id VARCHAR(255),
                            cust_unq_id VARCHAR(255) PRIMARY KEY,
                            cust_zipcode INT,
                            cust_city VARCHAR(20),
                            cust_state VARCHAR(20),
                            cust_name VARCHAR(255),
                            cust_timestamp TIMESTAMPTZ,
                            source VARCHAR(20),
                            batch_id VARCHAR(255));''')
            print('bronze customer table created')
        except Exception as e:
            print('customer table not created ',e)
            
# Geolocation table
def bronze_table_geolocation():
    with conn:
        try:
            cursor.execute('''CREATE TABLE IF NOT EXISTS geolocation(
                                geo_zipcode INT PRIMARY KEY,
                                geo_lat DOUBLE,
                                geo_lng DOUBLE,
                                geo_city VARCHAR(20),
                                geo_state VARCHAR(20),
                                geoloation_timestamp TIMESTAMPTZ,
                                source VARCHAR(20),
                                batch_id VARCHAR(255))''')
            print('bronze geolocation table created')
        except Exception as e:
            print('bronze geolocation table not created ',e)
            
# Orders table
def bronze_table_orders():
    with conn:
        try:
            cursor.execute('''CREATE TABLE IF NOT EXISTS orders(
                                order_id VARCHAR(255) PRIMARY KEY,
                                cust_id VARCHAR(255) REFERENCES customers(cust_id) ON DELETE CASCADE ON UPDATE CASCADE,
                                ord_status VARCHAR(30),
                                purchase_timestamp TIMESTAMP,
                                approved_at TIMESTAMP,
                                delivered_carrier_date TIMESTAMP,
                                delivered_customer_date TIMESTAMP,
                                estimated_delivery_date TIMESTAMP,
                                ord_timestamp TIMESTAMP,
                                source VARCHAR(20),
                                batch_id VARCHAR(255));''')
            print('bronze order table created')
        except Exception as e:
            print('order table not created ',e)

# OrderDetails table
def bronze_table_orderdetails():
    with conn:
        try:
            cursor.execute('''CREATE TABLE IF NOT EXISTS orddetails(
                                order_id VARCHAR(255) REFERENCES orders(order_id) ON DELETE CASCADE ON UPDATE CASCADE,
                                ord_itm_id INT,
                                prod_id VARCHAR(255) REFERENCES prod(prod_id) ON DELETE CASCADE ON UPDATE CASCADE,
                                seller_id VARCHAR(255) REFERENCES seller(seller_id) ON DELETE CASCADE ON UPDATE CASCADE,
                                shipp_limit_date TIMESTAMP,
                                price DOUBLE,
                                freight_val DOUBLE,
                                orddetail_timestamp TIMESTAMP,
                                source VARCHAR(20),
                                batch_id VARCHAR(255));''')
            print('orderdetails table got created')
        except Exception as e:
            print('orderdetails not created ',e)


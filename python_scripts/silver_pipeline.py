from python_scripts.extract_bronze import extract_bronze_data
from sql.load_silver import insert_silver_customer,insert_silver_geolocation,insert_silver_orddetails,insert_silver_sellers,insert_silver_prodEng,insert_silver_prod,insert_silver_orders,insert_silver_sellers,insert_silver_orddetails,insert_silver_payment,insert_silver_reviews
from python_scripts.silver_transform import customers_data,geolocation_data,orderDetails_data,orders_data,seller_data,review_data,prod_data,prodName_data,payment_data

# Creating datasets to make code clean
datasets = [
    ('prodEng',prodName_data,insert_silver_prodEng),
    ('geolocation',geolocation_data,insert_silver_geolocation),
    ('customers',customers_data,insert_silver_customer),
    ('sellers',seller_data,insert_silver_sellers),
    ('prod',prod_data,insert_silver_prod),
    ('orders',orders_data,insert_silver_orders),
    ('orddetails',orderDetails_data,insert_silver_orddetails)
    ('reviews',review_data,insert_silver_reviews),
    ('payment',payment_data,insert_silver_payment)
]

#df=extract_bronze_data('reviews')
#review_data(df)


# ETL Process
for table, transform_fun, load_fun in datasets:

    # Extract
    df = extract_bronze_data(table)

    # Transform
    df = transform_fun(df)

    # Load
    load_fun(df, table)

    print(f'{table} loaded successfully')
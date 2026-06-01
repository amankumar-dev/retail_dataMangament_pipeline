from python_scripts.extract_silver import extract_silver_data
from sql.load_gold import insert_dim_customer,insert_dim_date,insert_dim_location,insert_dim_prod,insert_dim_prodeng,insert_dim_seller,insert_fact_sales
from python_scripts.gold_transform import transform_sellers,transform_cust,transform_prod,transform_date,transform_fact,transform_location,transform_prodeng

# Creating datasets to make code clean
datasets = [
    #('customers','dim_cust',insert_dim_customer),
    #('geolocation','dim_location',insert_dim_location),
    #('sellers','dim_seller',insert_dim_seller),
    #('prodeng','dim_prodeng',insert_dim_prodeng),
    #('prod','dim_prod',insert_dim_prod),
    #('orddetails','dim_date',insert_dim_date)
]

ord_details=extract_silver_data('orders')
date_df=transform_date(ord_details)
insert_dim_date('dim_date',date_df)

# ETL Process
for exTable,table,transform_fun,load_fun in datasets:

    # Extract
    df = extract_silver_data(exTable)

    # Transform
    df = transform_fun(df)

    # Load
    load_fun(table,df)

    print(f'{table} loaded successfully')
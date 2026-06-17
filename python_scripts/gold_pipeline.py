from python_scripts.extract_silver import extract_silver_data
from sql.load_gold import insert_dim_customer,insert_dim_date,insert_dim_location,insert_dim_prod,insert_dim_prodeng,insert_dim_seller,insert_fact_sales
from python_scripts.gold_transform import transform_sellers,transform_cust,transform_prod,transform_date,transform_fact,transform_location,transform_prodeng

# Creating datasets to make code clean
datasets = [
    ('sellers',transform_sellers,'dim_seller',insert_dim_seller),
    ('customers',transform_cust,'dim_cust',insert_dim_customer),
    ('prodeng',transform_prodeng,'dim_prodeng',insert_dim_prodeng),
    ('prod',transform_prod,'dim_prod',insert_dim_prod),
    ('orders',transform_date,'dim_date',insert_dim_date),
    ('geolocation',transform_location,'dim_location',insert_dim_location),
    ('orders',transform_fact,'fact_sales',insert_fact_sales)
]

# ETL Process
for exTable,transform_fun,table,load_fun in datasets:

    # Extract
    df = extract_silver_data(exTable)

    # Transform
    df = transform_fun(df)
    
    # Write
    df.to_csv(f'/mnt/d/aman/aman.code/dataengproject/retail_management/datasets/gold/gold_{exTable}.csv')
    
    # Load
    load_fun(table,df)

    print(f'{table} loaded successfully')
    

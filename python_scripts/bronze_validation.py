from python_scripts.extract_bronze import extract_bronze_data

DATA_SETS=['prodeng','geolocation','customers','sellers','prod','orders','orddetails','reviews','payment']

EXPECTED_COL={
    'customers.csv':['cust_id','cust_unq_id','cust_zipcode','cust_city','cust_state','cust_name','timestampp','source','batch_id'],
    'products.csv':['prod_id','prod_cat_name','prod_name_len','prod_desc_len','prod_photos_qty','prod_weight_g','prod_length_cm','']
}

from python_scripts.extract_bronze import extract_bronze_data
import logging

EXPECTED_COL={
    'customers':['cust_id','cust_unq_id','cust_zipcode','cust_city','cust_state','cust_name','timestampp','source','batch_id'],
    'prod':['prod_id','prod_cat_name','prod_name_len','prod_desc_len','prod_photos_qty','prod_weight_g','prod_length_cm','prod_height_cm','prod_width_cm','timestampp','source','batch_id'],
    'geolocation':['geo_zipcode','geo_lat','geo_lng','geo_city','geo_state','timestampp','source','batch_id'],
    'sellers':['seller_id','seller_zipcode','seller_city','seller_state','timestampp','source','batch_id'],
    'prodeng':['prod_cat_name','prod_cat_name_eng','timestampp','source','batch_id'],
    'orders':['order_id','cust_id','ord_status','purchase_timestamp','approved_at','delivered_carrier_date','delivered_customer_date','estimated_delivery_date','timestampp','source','batch_id'],
    'orddetails':['order_id','order_item_id','prod_id','seller_id','shipp_limit_date','price','freight_val','timestampp','source','batch_id'],
    'reviews':['review_id','order_id','rev_score','rev_comment_title','rev_comment_message','rev_creation_date','rev_answer_timestamp','timestampp','source','batch_id'],
    'payment':['order_id','payment_seq','payment_type','payment_installments','payment_value','timestampp','source','batch_id']
}

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

log=logging.getLogger(__name__)

def validation_bronze():
    for table,cols in EXPECTED_COL.items():
        df=extract_bronze_data(table)
        
        # Check empty
        if df.empty:
            log.error(f'{table} is empty')
            raise ValueError(f'{table} is empty')
        else:
            log.info(f'{table} is not empty')
        
        # Check column
        missing_cols=set(cols)-set(df.columns)
        if missing_cols:
            log.error(f'{table} does not have {missing_cols} column')
            raise ValueError(f'{table} does not have {missing_cols} column')
        else:
            log.info(f'{table} columns are fine')


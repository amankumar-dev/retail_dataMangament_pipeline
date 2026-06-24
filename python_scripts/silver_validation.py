from python_scripts.extract_silver import extract_silver_data
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

log=logging.getLogger(__name__)

DATA_SETS=['customers','orders','reviews']

def silver_cust_validation(df):
    # Check null value
    if df['cust_unq_id'].isna().any():
        log.error('cust_unq_id have null value')
        raise ValueError('cust_unq_id have null value')
    
    # Check duplicate value
    if df['cust_unq_id'].duplicated().any():
        log.error('cust_unq_id have duplicated value')
        raise ValueError('cust_unq_id have duplicated value')
    
def silver_orders_validation(df):
    # Check null value
    if df['order_id'].isna().any():
        log.error('order_id have null value')
        raise ValueError('order_id have null value')
    
    # Check duplicate value
    if df['order_id'].duplicated().any():
        log.error('order_id have duplicated value')
        raise ValueError('order_id have duplicated value')
    
def silver_review_validation(df):
    # Check rev_score
    if not df['rev_score'].between(1,5).all():
        log.error('review scores are unexpected')
        raise ValueError('review scores are unexpected')
    
VALIDATORS = {
    'customers': silver_cust_validation,
    'orders': silver_orders_validation,
    'reviews': silver_review_validation
}

def validation_silver():
    for table in DATA_SETS:
        df=extract_silver_data(table)
        VALIDATORS[table](df)
        log.info(f'{table} validation passed')

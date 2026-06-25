import pandas as pd
import logging
from sql.connection import conn

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

log=logging.getLogger(__name__)

def validation_gold():
    df=pd.read_sql('''SELECT * FROM gold.fact_sales''',conn)
    
    quality_issue=False
    
    # Check emptiness
    if df.empty:
        log.error('fact_sales have no values')
        raise ValueError('fact_sales have no values')
    
    if df[['cust_sk','prod_sk','seller_sk','date_sk']].isna().any().any():
        log.warning('Surrogate key have nulls value')
        quality_issue=True
        
    if df[['order_sk','prod_sk']].duplicated().any():
        log.warning('fact_sales have duplicated value')
        quality_issue=True
    
    if (df['payment_val']<0).any():
        log.warning('Payment has negative value')
        quality_issue=True
    
    if not df['rev_score'].between(1,5).all():
        log.warning('Review score is not in range')
        quality_issue=True
        
    if quality_issue:
        log.warning('Gold validation complete with warnings')
    else:
        log.info('Gold validation passed')

validation_gold()
import pandas as pd
import logging

DATA_SETS=[]

VALIDATORS={
    
}

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

log=logging.getLogger(__name__)

def fact_sales_validation(df):
    # Check emptiness
    if df.empty:
        log.error('fact_sales have no values')
        raise ValueError('fact_sales have no values')
    
    if df['']
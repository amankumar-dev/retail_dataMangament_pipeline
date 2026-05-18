# For transforming the raw data
import pandas as pd
from python_scripts.silver_pipeline import customers

def customers_data(df):
    # Remove duplicates values
    pass

print(customers[customers.duplicated(['cust_id'])])
import pandas as pd
from python_scripts.extract_silver import extract_silver_data

df=extract_silver_data('sellers')
print(df.head(5))

# For sellers table
def transform_sellers(df)
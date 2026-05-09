import pandas as pd

customers = pd.read_csv(
    "datasets/raw/olist_customers_dataset.csv"
)

print(customers.head())

print(customers.info())
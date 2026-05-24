from python_scripts.extract_bronze import extract_bronze_data

# Fetching data from bronze schema
customers=extract_bronze_data('customers')
geolocation=extract_bronze_data('geolocation')
orddetails=extract_bronze_data('orddetails')
orders=extract_bronze_data('orders')
payment=extract_bronze_data('payment')
productName=extract_bronze_data('prodEng')
products=extract_bronze_data('prod')
reviews=extract_bronze_data('reviews')
sellers=extract_bronze_data('sellers')


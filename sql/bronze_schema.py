from connection import conn,cursor

# Create bronze schema
def create_bronze_schema():
    with conn:
        try:
            cursor.execute('''CREATE SCHEMA IF NOT EXIST bronze
                           ''')
            print('bronze schema created')
        except Exception as e:
            print(e)

# Create bronze tables

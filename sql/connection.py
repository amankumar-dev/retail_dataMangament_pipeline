import os
from dotenv import load_dotenv
import psycopg2

load_dotenv(".env")

# Creating Connection with postgresql
def get_connection():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        return conn
    except Exception as e:
        print("Database doesn't connected ",e)
        return None

conn=get_connection()
if conn:
    print('Connection established successfully')
else:
    print('Connection Failed!!')
    
cursor=conn.cursor()
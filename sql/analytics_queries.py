from sql.connection import conn,cursor

def total_rev():
    with conn:
        try:
            cursor.execute('''SELECT SUM(price+freight_val)
                                AS total_rev
                                FROM gold.fact_sales;''')
            result=cursor.fetchone()
            return result
        except Exception as e:
            print('total reveneue not fetched ',e)
            
def monthly_rev():
    with conn:
        try:
            cursor.execute('''SELECT
                                d.month,
                                d.year,
                                SUM(price+freight_val)
                                FROM gold.fact_sales f
                                JOIN gold.dim_date d
                                ON f.date_sk=d.date_sk
                                GROUP BY d.month,d.year
                                ORDER BY d.month,d.year;''')
            result=cursor.fetchall()
            return result
        except Exception as e:
            print('monthly reveneue not fetched ',e)
            
def yearly_rev():
    with conn:
        try:
            cursor.execute('''SELECT
	                            d.year,
                                SUM(f.price+f.freight_val)
	                            FROM gold.fact_sales f
	                            JOIN gold.dim_date d
	                            ON f.date_sk=d.date_sk
	                            GROUP BY d.year
	                            ORDER BY d.year;''')
            result=cursor.fetchall()
            return result
        except Exception as e:
            print('monthly reveneue not fetched ',e)
            
def state_rev():
    with conn:
        try:
            cursor.execute('''SELECT
	                            c.cust_state,
	                            SUM(f.price+f.freight_val) AS total_rev
	                            FROM gold.fact_sales f
	                            JOIN gold.dim_cust c
	                            ON f.cust_sk=c.cust_sk
	                            GROUP BY c.cust_state
	                            ORDER BY total_rev;''')
            result=cursor.fetchall()
            return result
        except Exception as e:
            print('state reveneue not fetched ',e)
            

#data=total_rev()
#print(data)
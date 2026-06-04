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
            
def prod_rev():
    with conn:
        try:
            cursor.execute('''SELECT
	                            p.prod_cat_name,
	                            SUM(f.price+f.freight_val) AS total_rev
	                            FROM gold.fact_sales f
	                            LEFT JOIN gold.dim_prod p
	                            ON f.prod_sk=p.prod_sk
	                            GROUP BY p.prod_cat_name
	                            ORDER BY total_rev DESC;''')
            result=cursor.fetchall()
            return result
        except Exception as e:
            print('state reveneue not fetched ',e)
            
def avg_rev():
    with conn:
        try:
            cursor.execute('''SELECT
                                SUM(price + freight_val) /
                                COUNT(DISTINCT order_sk) AS avg_order_value
                                FROM gold.fact_sales;''')
            result=cursor.fetchone()
            return result
        except Exception as e:
            print('state reveneue not fetched ',e)
            
def top_cust():
    with conn:
        try:
            cursor.execute('''SELECT
	                            f.cust_sk AS cust_id,
	                            c.cust_name,
	                            SUM(f.price+f.freight_val) AS total_ord_amnt
	                            FROM gold.fact_sales f
	                            JOIN silver.customers c
	                            ON f.cust_sk=c.cust_sk
	                            GROUP BY f.cust_sk,c.cust_name
	                            ORDER BY total_ord_amnt DESC
	                            LIMIT 5;''')
            result=cursor.fetchall()
            return result
        except Exception as e:
            print('state reveneue not fetched ',e)

def repeat_cust():
    with conn:
        try:
            cursor.execute('''SELECT
	                            f.cust_sk AS cust_id,
	                            c.cust_name,
	                            COUNT(DISTINCT order_sk) AS repeated
	                            FROM gold.fact_sales f
	                            JOIN silver.customers c
	                            ON f.cust_sk=c.cust_sk
	                            GROUP BY f.cust_sk,c.cust_name
	                            HAVING (COUNT(DISTINCT order_sk))>1
	                            ORDER BY repeated DESC
	                            LIMIT 5;''')
            result=cursor.fetchall()
            return result
        except Exception as e:
            print('state reveneue not fetched ',e)

def rev_per_cust():
    with conn:
        try:
            cursor.execute('''SELECT
	                            SUM(price+freight_val)/COUNT(DISTINCT(cust_sk)) rev_per_cust
	                            FROM gold.fact_sales;''')
            result=cursor.fetchone()
            return result
        except Exception as e:
            print('state reveneue not fetched ',e)

def return_vs_new_cust():
    with conn:
        try:
            cursor.execute('''SELECT
	                            CASE
		                            WHEN total_orders = 1 THEN 'New'
		                            ELSE 'Returning'
	                                END AS customer_type,
	                                COUNT(*) AS no_of_cust
	                            FROM(SELECT
			                            cust_sk,
			                            COUNT(DISTINCT order_sk) AS total_orders
			                            FROM gold.fact_sales
			                            GROUP BY cust_sk
		                            ) t
	                            GROUP BY customer_type;''')
            result=cursor.fetchall()
            return result
        except Exception as e:
            print('state reveneue not fetched ',e)
            
#data=total_rev()
#print(data)
import pandas as pd
from sql.analytics_queries import top_cust,repeat_cust,rev_per_cust,return_vs_new_cust

def get_top_customers():
    result=top_cust()
    df=pd.DataFrame(
        result,
        columns=['Cust_id','Cust_name','Revenue']
    )
    df['Cust_name']=df['Cust_name'].str.title()
    df['Revenue']=(df['Revenue']/100000).map('₹{:.2f} l'.format)
    print(df)
    
def get_repeat_customers():
    result=repeat_cust()
    df=pd.DataFrame(
        result,
        columns=['Cust_id','Cust_name','Orders']
    )
    df['Cust_name']=df['Cust_name'].str.title()
    print(df)

def get_revenue_per_customer():
    result=rev_per_cust()[0]
    print(f'Revenue Per Customer: ₹{result:.2f}.')
    
def get_new_vs_returning_customers():
    result=return_vs_new_cust()
    df=pd.DataFrame(
        result,
        columns=['Cust_Type','No_of_Cust']
    )
    print(df)
    

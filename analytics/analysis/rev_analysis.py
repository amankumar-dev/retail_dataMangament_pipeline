from sql.analytics_queries import total_rev,monthly_rev,yearly_rev,state_rev
import calendar
import pandas as pd
import numpy as np

MONTH_MAP = dict(enumerate(calendar.month_abbr))

def get_total_revenue():
    result=total_rev()[0]
    print(f'Total Revenue: ₹{float(result/10000000):.2f} cr.')

def get_monthly_revenue():
    result=monthly_rev()
    df=pd.DataFrame(
        result,
        columns=['Month','Year','Revenue']
    )
    df['Month']=df['Month'].map(MONTH_MAP)
    df['Revenue']=(df['Revenue']/1000).map('₹{:.2f} k'.format)
    
    print(df)

def get_yearly_revenue():
    result=yearly_rev()
    df=pd.DataFrame(
        result,
        columns=['Year','Revenue']
    )
    df['Revenue']=(df['Revenue']/1000).map('₹{:.2f} k'.format)
    print(df)
    
def get_revenue_by_state():
    result=state_rev()
    df=pd.DataFrame(
        result,
        columns=['State','Revenue']
    )
    df['Revenue']=(df['Revenue']/1000).map('₹{:.2f} k'.format)
    print(df)

#get_revenue_by_category()

#get_average_order_value()

#get_total_revenue()
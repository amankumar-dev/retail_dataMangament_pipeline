from sql.analytics_queries import yearly_rev,monthly_rev,quarterly_rev,weekday_rev,weekday_vs_weekend
import pandas as pd
import calendar

MONTH_MAP = dict(enumerate(calendar.month_abbr))

def get_revenue_by_year():
    result=yearly_rev()
    df=pd.DataFrame(
        result,
        columns=['Year','Revenue']
    )
    df['Revenue']=(df['Revenue']/1000).map('₹{:.2f} k'.format)
    return df

def get_revenue_by_month():
    result=monthly_rev()
    df=pd.DataFrame(
        result,
        columns=['Month','Year','Revenue']
    )
    df['Month']=df['Month'].map(MONTH_MAP)
    df['Revenue']=(df['Revenue']/1000).map('₹{:.2f} k'.format)
    return df

def get_revenue_by_quarter():
    result=quarterly_rev()
    df=pd.DataFrame(
        result,
        columns=['Quarter','Revenue']
    )
    df['Revenue']=(df['Revenue']/100000).map('₹{:.2f} l'.format)
    return df

def get_weekday_sales():
    result=weekday_rev()
    df=pd.DataFrame(
        result,
        columns=['Weekday','Revenue']
    )
    df['Revenue']=(df['Revenue']/100000).map('₹{:.2f} l'.format)
    return df    

def get_weekend_vs_weekday_sales():
    result=weekday_vs_weekend()
    df=pd.DataFrame(
        result,
        columns=['Day Type','Revenue']
    )
    df['Revenue']=(df['Revenue']/100000).map('₹{:.2f} l'.format)
    return df
    
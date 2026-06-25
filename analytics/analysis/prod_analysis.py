import pandas as pd
from sql.analytics_queries import top_selling_prod,least_selling_prod,top_rev_prod,cat_perform,prod_cont

def get_top_selling_prod_cat():
    result=top_selling_prod()
    df=pd.DataFrame(
        result,
        columns=['Prod_name','Sold']
    )
    df['Prod_name']=df['Prod_name'].str.title()
    return df

def get_least_selling_prod_cat():
    result=least_selling_prod()
    df=pd.DataFrame(
        result,
        columns=['Prod_id','Prod_name','Sold']
    )
    df['Prod_name']=df['Prod_name'].str.title()
    return df

def get_top_revenue_products():
    result=top_rev_prod()
    df=pd.DataFrame(
        result,
        columns=['Prod_id','Revenue']
    )
    df['Revenue']=(df['Revenue']/1000).map('₹{:.2f} k'.format)
    return df
    
def get_category_performance():
    result=cat_perform()
    df=pd.DataFrame(
        result,
        columns=['Product Category','Revenue','Total Orders','Units Sold']
    )
    df['Revenue']=(df['Revenue']/1000)
    df['Product Category']=df['Product Category'].str.title()
    return df

def get_product_contribution():
    result=prod_cont()
    df=pd.DataFrame(
        result,
        columns=['Product Category','Revenue','Contribution']
    )
    df['Revenue']=(df['Revenue']/100000)
    df['Product Category']=df['Product Category'].str.title()
    return df
    
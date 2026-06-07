import matplotlib.pyplot as plt
from analytics.analysis.cust_analysis import get_new_vs_returning_customers

def cust_analysis_chart():
    df=get_new_vs_returning_customers()
    
    plt.figure(figsize=(4,2))
    
    plt.bar(df['Cust_Type'],df['No_of_Cust'],width=0.4)
    plt.xlabel('Customer Type')
    plt.ylabel('No. Of Customer')
    
    plt.title('New Customer VS Returning Customer')
    
    plt.tight_layout()
    plt.savefig(
        "analytics/reports/cust_analysis.png",
        bbox_inches="tight"
    )
    
    plt.close()
    
cust_analysis_chart()
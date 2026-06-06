from analytics.analysis.rev_analysis import get_monthly_revenue,get_yearly_revenue
import matplotlib.pyplot as plt

def monthly_rev_chart():
    df=get_monthly_revenue()

    plt.figure(figsize=(10,5))
    plt.plot(df['Month'],df['Revenue'],marker='o')

    plt.title('Monthly Revenue Trend')
    plt.xlabel('Month')
    plt.ylabel('Revenue')

    plt.tight_layout()

    plt.savefig(
        "analytics/reports/monthly_revenue.png",
        bbox_inches="tight"
    )
    plt.close()

def yearly_rev_chart():
    df=get_yearly_revenue()
    
    plt.figure(figsize=(5,3))
    plt.bar(df['Year'].astype(str),df['Revenue'],width=0.2)
    
    plt.title('Yearly Revenue')
    plt.xlabel('Year')
    plt.ylabel('Revenue')
    
    plt.tight_layout()
    
    plt.savefig(
        "analytics/reports/yearly_revenue.png",
        bbox_inches="tight"
    )
    plt.close()

monthly_rev_chart()
yearly_rev_chart()
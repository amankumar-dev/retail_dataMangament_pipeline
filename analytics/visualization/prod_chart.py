import matplotlib.pyplot as plt
from analytics.analysis.prod_analysis import get_category_performance,get_product_contribution

def cat_perf_chart():
    df=get_category_performance()
    df = df.sort_values('Revenue', ascending=False)

    plt.figure(figsize=(12,6))
    plt.barh(
        df['Product Category'],
        df['Revenue']
    )      

    plt.title('Revenue by Product Category')
    plt.xlabel('Revenue (K)')
    plt.ylabel('Category')

    plt.tight_layout()
    plt.savefig(
        "analytics/reports/category_rev.png",
        bbox_inches="tight"
    )
    plt.close()
    
def prod_contr_chart():
    df = get_product_contribution()

    plt.figure(figsize=(8,8))

    plt.pie(
        df['Contribution'],
        labels=df['Product Category'],
        autopct='%1.1f%%'
    )

    plt.title('Product Category Revenue Contribution')

    plt.savefig(
        'analytics/reports/product_contribution.png',
        bbox_inches='tight'
    )

    plt.close()
    
def prod_chart():
    prod_contr_chart()
    cat_perf_chart()
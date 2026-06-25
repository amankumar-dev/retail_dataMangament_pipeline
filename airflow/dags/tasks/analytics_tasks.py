from airflow.decorators import task
from datetime import timedelta
import logging
from analytics.analysis.cust_analysis import get_top_customers,get_repeat_customers,get_revenue_per_customer
from analytics.analysis.rev_analysis import get_monthly_revenue,get_revenue_by_state
from analytics.analysis.prod_analysis import get_product_contribution

log=logging.getLogger(__name__)

@task(retries=3,retry_delay=timedelta(minutes=5))
def analytics_task():
    top_cust=get_top_customers()
    repeat_cust=get_repeat_customers()
    rev_per_cust=get_revenue_per_customer()
    monthly_rev=get_monthly_revenue()
    state_rev=get_revenue_by_state()
    prod_contribution=get_product_contribution()
    
    top_cust.to_csv(
        "analytics/reports/top_customers.csv",
        index=False
    )

    repeat_cust.to_csv(
        "analytics/reports/repeat_customers.csv",
        index=False
    )
    
    rev_per_cust.to_csv(
        "analytics/reports/revenue_per_customer.csv",
        index=False
    )

    monthly_rev.to_csv(
        "analytics/reports/monthly_revenue.csv",
        index=False
    )

    state_rev.to_csv(
        "analytics/reports/state_revenue.csv",
        index=False
    )
    
    prod_contribution.to_csv(
        "analytics/reports/product_contribution.csv",
        index=False
    )
    
    log.info("Analytics completed")
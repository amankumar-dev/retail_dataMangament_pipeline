from airflow.decorators import task
from datetime import timedelta
from analytics.visualization.cust_chart import cust_chart
from analytics.visualization.prod_chart import prod_chart
from analytics.visualization.rev_chart import rev_chart

@task(retries=3,retry_delay=timedelta(minutes=5))
def report_task():
    cust_chart()
    prod_chart()
    rev_chart()
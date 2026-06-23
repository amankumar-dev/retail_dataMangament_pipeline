from airflow.sdk import task
from datetime import datetime,timedelta

@task(retries=3,retry_delay=timedelta(minutes=5))
def silver_task():
    from python_scripts.silver_pipeline import silver_pipeline
    silver_pipeline()

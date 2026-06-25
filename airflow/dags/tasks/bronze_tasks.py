from airflow.decorators import task
from datetime import datetime,timedelta

@task(retries=3,retry_delay=timedelta(minutes=5))
def bronze_task():
    from python_scripts.bronze_pipeline import bronze_pipeline
    bronze_pipeline()
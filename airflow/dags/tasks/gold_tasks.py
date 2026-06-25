from python_scripts.gold_pipeline import gold_pipeline
from airflow.decorators import task
from datetime import timedelta

@task(retries=3,retry_delay=timedelta(minutes=5))
def gold_task():
    gold_pipeline()
from airflow.sdk import task
from python_scripts.bronze_validation import validation_bronze
from datetime import datetime, timedelta

@task(retries=3,retry_delay=timedelta(minutes=5))
def validate_bronze_task():
    validation_bronze()
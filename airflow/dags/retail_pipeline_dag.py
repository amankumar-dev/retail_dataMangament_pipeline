from airflow.sdk import dag,task
from datetime import datetime
from tasks.sensors import wait_bronze
from tasks.bronze_tasks import bronze_task
from tasks.validation_tasks import validate_bronze_task
from tasks.silver_tasks import silver_task


# Create DAG
@dag(
    dag_id='retail_pipeline',
    start_date=datetime(2026,6,22),
    schedule="@daily",
    catchup=False
)

# Create Taskflow API
def retail_pipeline():
    
    # For bronze raw file exist
    bronze_files=wait_bronze()
    
    # For load bronze file
    load_bronze=bronze_task()
    
    # Validate bronze 
    validate_bronze=validate_bronze_task()
    
    # For load silver file
    load_silver=silver_task()
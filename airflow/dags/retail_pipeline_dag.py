from airflow.sdk import dag,task
from datetime import datetime
from dags.tasks.sensors import wait_bronze
from dags.tasks.bronze_tasks import bronze_task


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
from airflow.decorators import dag
from datetime import datetime
from tasks.sensors import wait_bronze
from tasks.bronze_tasks import bronze_task
from tasks.validation_tasks import validate_bronze_task,validate_silver_task,validate_gold_task
from tasks.silver_tasks import silver_task
from tasks.gold_tasks import gold_task
from tasks.analytics_tasks import analytics_task
from tasks.reports_tasks import report_task


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
    
    # Validate Silver
    validate_silver=validate_silver_task()
    
    # For load gold file
    load_gold=gold_task()
    
    # Validate Gold
    validate_gold=validate_gold_task()
    
    # Analytics task
    task_analytics=analytics_task()
    
    # Reports task
    task_report=report_task()
    
    (
        bronze_files
        >> load_bronze
        >> validate_bronze
        >> load_silver
        >> validate_silver
        >> load_gold
        >> validate_gold
        >> task_analytics
        >> task_report
    )
        

retail_pipeline()
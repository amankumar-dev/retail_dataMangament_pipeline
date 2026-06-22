from airflow.sdk import task

@task
def bronze_task():
    from python_scripts.bronze_pipeline import bronze_pipeline
    bronze_pipeline()
import sys
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

# Add the path to your project directory to sys.path

sys.path.insert(0, '/home/ubuntu/Desktop/data_viz_project/data_pipeline')

# Now, you should be able to import modules from your project
from web_scraper.web_scraper import scrape_earthquake_data
from data_processor.data_processor import process_data
from storage_loader.mongo_util import get_spark_session

# Define default_args to specify the start date, schedule interval, and other DAG parameters
default_args = {
    'owner': 'your_name',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Instantiate the DAG
dag = DAG(
    'earthquake_data_processing',
    default_args=default_args,
    description='DAG for processing earthquake data',
    schedule_interval=timedelta(days=1),  # Set the schedule interval based on your needs
)

# Define a PythonOperator to execute the web scraping task
scrape_data_task = PythonOperator(
    task_id='scrape_data_task',
    python_callable=scrape_earthquake_data,
    provide_context=False,
    dag=dag,
)

# Define a PythonOperator to execute the data processing task
process_data_task = PythonOperator(
    task_id='process_data_task',
    python_callable=process_data,
    provide_context=False,
    op_args=[get_spark_session()],
    dag=dag,
)

# Set task dependencies
scrape_data_task >> process_data_task

if __name__ == "__main__":
    dag.cli()


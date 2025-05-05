#import libraries
from airflow.operators.python import PythonOperator
from airflow import DAG
from datetime import timedelta
from ETL import extract, transform, load

default_args={
     'owner': 'Cley',
     'start_date': timedelta(days=1),
     'retries': 1,
     'retry_delay': timedelta(minutes=5),
}

dag = DAG(
     dag_id='weather_etl',
     default_args=default_args,
     description='Weather Data Pipeline',
     schedule=timedelta(minutes=1),
)

extract_task = PythonOperator(
    task_id='extract',
    python_callable=extract,
    dag=dag,
)

transform_task = PythonOperator(
    task_id='transform',
    python_callable=lambda: transform(extract()),
    dag=dag,
)

load_task = PythonOperator(
    task_id='load',
    python_callable=load,
    dag=dag,
)

extract_task >> transform_task >> load_task
from airflow import DAG
from datetime import datetime, timedelta
from airflow.sensors.http_sensor import http_sensor
default_args={
    "owner":"airflow",
    "start_date": datetime(2020,12,12),
    "depends_on_past":False,
    "email_on_failure":False,
    "email_on_retry":False,
    "email":"youremail@gmail.com",
    "retries":1,
    "retry_delay":timedelta(minutes=5)
}

with DAG(dag_id="forex_data_pipeline",
schedule_interval="@daily",
default_args=default_args,
catchup=False,
) as dag:

is_foreex
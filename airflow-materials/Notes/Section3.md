### Lect 18
##### What is DAG


##### Important Properties

* dag_id --> unique identifier of your DAG
* description --> the description of your DAG
* start_Date --> indicates from which date your DAG should start.
* schedule_interval --> defines how often your DAG runs from the start_date.
* default_args --> a dictionary containing parameters that will be applied to all operators and so to your tasks.
* catchup --> to perform scheduler catchup (True by default).

===============

Ongoing
### Lect 19
##### Defining your first DAG

{Video 8}


### Lect 20
##### What is an Operator?


### Lect 21 HTTP sensor
http://exchangeratesapi.io/

https://api.exchangeratesapi.io/latest?base=USD


https://airflow.readthedocs.io/en/stable/_modules/airflow/sensors/http_sensor.html


forex_data_pipeline_v_2.py

./start.sh

localhost:8080
    click>admin>connection
        Conn ID: forex_api
        Conn Type : Http
        Host : http://api.exchangeratesapi.io/
        >Then click save


docker exec -it <containerID> /bin/bash

airflow test forex_data_pipeline is_forex_Rates_available 2012-12-10 

airflow test forex_data_pipeline is_forex_rates_available 2020-12-10
-------    

### Lect 22 FileSensor 
File sensor 




## to  run docker File
docker build -t airflow-basic .


## to list all docker images
docker image ls

### to run docker

docker run --rm -d  -p  8080:8080 airflow-basic

localhost:8080


docker run -p 8080:8080 -d airflow-basic

### if you want to change port like web_server_port=8080 to other

docker exec -it `<containter>`  /bin/bash

##### change it 
Now to quit
:q , then press control +D

------

Lect 12
=================


#### airflow command

```


Chandras-MacBook-Pro:airflow-materials ckgauro$ docker exec -it c987ffa7b49b /bin/bash
airflow@c987ffa7b49b:~$ pwd
/usr/local/airflow
airflow@c987ffa7b49b:~$ 

airflow initdb
* Initialise the metadatabase


airflow resetdb
* Reinitialize the metadatabase (Drop everything)


airflow upgradedb
* Upgrade the metadatabase (Latest schemas, values, ...)


airflow webserver
* Start Airflow’s webserver
* airflow webserver  -p -w -d 

airflow scheduler
* Start Airflow’s scheduler
* airflow scheduler -d  -sd 


airflow worker
* Start a Celery worker (Useful in distributed mode to spread tasks among nodes - machines)


```

Lect 13
=================


#### Controlling your DAGs with the CLI

```

* Give the list of known dags (either those in the examples folder or in dags folder)
airflow list_dags

* Display the files/folders of the current directory 
ls
ls /usr/local/lib/python3.8/site-packages/airflow/example_dags
localhost:8080 
    click tutorial>Details
        Select filtepath



airflow trigger_dag example_python_operator
* Trigger the dag example_python_operator with the current date as execution date


airflow trigger_dag example_python_operator -e 2015-03-02
* Trigger the dag example_python_operator with a date in the past as execution date (This won’t trigger the tasks of that dag unless you set the option catchup=True in the DAG definition)


airflow trigger_dag example_python_operator -e '2019-07-08 19:04:00+00:00'
* Trigger the dag example_python_operator with a date in the future (change the date here with one having +2 minutes later than the current date displayed in the Airflow UI). The dag will be scheduled at that date.


airflow list_dag_runs example_python_operator
* Display the history of example_python_operator’s dag runs


airflow list_tasks example_python_operator
* List the tasks contained into the example_python_operator dag


airflow test example_python_operator print_the_context 2018-05-07
* Allow to test a task (print_the_context) from a given dag (example_python_operator here) without taking care of dependencies and past runs. Useful for debugging.

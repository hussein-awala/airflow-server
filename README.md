# Airflow server

This project contains a [docker-compose](https://docs.docker.com/compose/) file, and some docker configurations to
deploy an airflow server with local executor for testing/development.

## Customize your airflow docker image

To install your python packages and use them in the dags, you can add them to the
[requirements.txt](docker/requirements.txt) file, and you can update the [Dockerfile](docker/Dockerfile)
as you need.

## Airflow webserver credentials

In this project version, we configure the airflow webserver credentials in the
[docker compose file](docker-compose.yml) which we provide as environment variables for the  which you can
update it to add your user infos.
```dotenv
_AIRFLOW_WWW_USER_USERNAME: airflow_user
_AIRFLOW_WWW_USER_FIRSTNAME: Airflow
_AIRFLOW_WWW_USER_LASTNME: Admin
_AIRFLOW_WWW_USER_EMAIL: airflowadmin@example.com
_AIRFLOW_WWW_USER_ROLE: Admin
_AIRFLOW_WWW_USER_PASSWORD: airflow_password
```

## Deploy the airflow server
Before deploying the server, make sure you have the folders dags, db, logs, and scripts which are attached to some
docker services.
```shell
# choose your airflow version
export AIRFLOW_VERSION=2.2.4
docker-compose up -d --build
```
Finally, in the browser, open `http://localhost:8080` and put the username and password you used in
[this step](#airflow-webserver-credentials) and click on login.
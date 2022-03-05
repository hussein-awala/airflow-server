ARG AIRFLOW_VERSION=2.2.4

FROM apache/airflow:${AIRFLOW_VERSION}
WORKDIR /airflow
COPY requirements.txt /airflow/requirements.txt
RUN pip install -r /airflow/requirements.txt

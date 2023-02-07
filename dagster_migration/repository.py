import os

from dagster_airflow import make_dagster_definitions_from_airflow_dags_path

migrated_dags = make_dagster_definitions_from_airflow_dags_path(
    os.path.abspath("./dags/"))

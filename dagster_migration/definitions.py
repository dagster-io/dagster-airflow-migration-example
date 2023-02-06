import os

from dagster_airflow.dagster_pipeline_factory import \
    make_dagster_repo_from_airflow_dags_path

migrated_dags = make_dagster_repo_from_airflow_dags_path(
    os.path.abspath("./dags/"),
    "migrated_dags",
)

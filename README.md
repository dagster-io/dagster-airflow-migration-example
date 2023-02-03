# dagster-airflow-migration-example

an example of doing a lift-and-shift migration of airflow to dagster using the [dagster-airflow integration library](https://docs.dagster.io/integrations/airflow)


## to run as airflow

```bash

docker-compose build

docker-compose up

```


## to run as dagster

```bash

pip install -e ".[dev]"

dagster dev

```
## to run on dagster-cloud 

```bash

pip install -e ".[dev]"
pip install dagster-cloud


dagster-cloud serverless deploy \
      --location-name dagster_migration  \
      --package-name  dagster_migration
```

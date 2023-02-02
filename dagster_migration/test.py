import time
from datetime import date, timedelta

from dagster import RetryPolicy, ScheduleDefinition, job, op, repository


@op
def print_date():
    dt = date.today()
    print(dt)
    return dt

@op(
    retry_policy=RetryPolicy(
        max_retries=3
    )
)
def sleep(dt: date):
    time.sleep(5)

@op
def templated(dt: date):
    for i in range(5):
        print(dt)
        print(dt - timedelta(days=7))

@job(tags={"dagster/max_retries": 1, "dag_name": "example"})
def tutorial_job():
    dt = print_date()
    sleep(dt)
    templated(dt)

schedule = ScheduleDefinition(job=tutorial_job, cron_schedule="@daily")

@repository
def rewrite_repo():
    return [tutorial_job, schedule]

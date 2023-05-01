from setuptools import find_packages, setup

setup(
    name="airflow-dagster-migration",
    packages=find_packages(),
    install_requires=[
        "dagster>=1.0.0",
        "dagster_airflow>=0.17.5",
        "apache-airflow==2.5.2",
        "dagster_cloud>=1.0.0",
    ],
    extras_require={"dev": ["dagit", "pytest"]},
)

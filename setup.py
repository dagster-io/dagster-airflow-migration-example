from setuptools import find_packages, setup

setup(
    name="airflow-dagster-migration",
    packages=find_packages(),
    install_requires=[
        "dagster>=1.0.0",
        "dagster_airflow>=0.17.5",
        "apache-airflow==2.5.0",
        "dagster_cloud>=1.0.0",
        # airflow dag specific dependencies
        "docker>=5.0.3,<6.0.0",
        "apache-airflow-providers-docker>=3.2.0,<4",
        "apache-airflow-providers-apache-spark>=3.0.0,<4",
        "kubernetes>=10.0.1",
    ],
    extras_require={"dev": ["dagit", "pytest"]},
)

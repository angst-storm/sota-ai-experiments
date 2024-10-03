from airflow.decorators import dag
from airflow.providers.cncf.kubernetes.operators.spark_kubernetes import SparkKubernetesOperator
from airflow.providers.cncf.kubernetes.sensors.spark_kubernetes import SparkKubernetesSensor
from airflow.template.templater import LiteralValue

@dag()
def spark_operator():
    submit = SparkKubernetesOperator(
        task_id="submit",
        namespace="airflow",
        application_file=LiteralValue("dags/sparkapp.yaml")
    )

    submit

spark_operator()
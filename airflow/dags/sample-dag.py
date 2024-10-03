from airflow.decorators import dag
from datetime import datetime
from airflow.providers.cncf.kubernetes.operators.spark_kubernetes import SparkKubernetesOperator
from airflow.providers.cncf.kubernetes.sensors.spark_kubernetes import SparkKubernetesSensor

@dag(start_date=datetime(2024, 1, 1), schedule="@daily")
def spark_operator():
   submit = SparkKubernetesOperator(
        task_id="spark-pi",
        namespace="spark-operator",
        application_file="sparkapp.yaml",
        do_xcom_push=True,
        params={"app_name": "spark-pi"},
    )

   submit_sensor = SparkKubernetesSensor(
        task_id="submit_sensor",
        namespace="spark-operator",
        application_name="{{ task_instance.xcom_pull(task_ids='submit')['metadata']['name'] }}",
        attach_log=True,
   )

   submit >> submit_sensor

spark_operator()
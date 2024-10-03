from airflow.decorators import dag
from airflow.providers.cncf.kubernetes.operators.spark_kubernetes import SparkKubernetesOperator

@dag()
def spark_operator():
   SparkKubernetesOperator(
        task_id="spark-pi",
        namespace="spark-operator",
        application_file="sparkapp.yaml",
        do_xcom_push=True
    )

spark_operator()
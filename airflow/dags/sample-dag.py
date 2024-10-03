from airflow.decorators import dag
from airflow.providers.cncf.kubernetes.operators.spark_kubernetes import SparkKubernetesOperator
from airflow.providers.cncf.kubernetes.sensors.spark_kubernetes import SparkKubernetesSensor

@dag()
def spark_operator():
    submit = SparkKubernetesOperator(
        task_id="submit",
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
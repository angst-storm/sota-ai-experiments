from airflow.decorators import dag
from airflow.providers.cncf.kubernetes.operators.spark_kubernetes import SparkKubernetesOperator
from airflow.providers.cncf.kubernetes.sensors.spark_kubernetes import SparkKubernetesSensor
from airflow.template.templater import LiteralValue
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.operators.email import EmailOperator
from airflow.utils.trigger_rule import TriggerRule

@dag()
def sample_dag():
    postgres = PostgresOperator(
        task_id='postgres',
        postgres_conn_id='pg',
        sql='SELECT 1'
    )

    spark_pi = SparkKubernetesOperator(
        task_id="spark_pi",
        namespace="airflow",
        application_file=LiteralValue("dags/sparkapp.yaml")
    )

    email = EmailOperator(
        task_id='send_email',
        to='{{ var.value.admin_email }}',
        subject='Внимание!',
        html_content='<p>Все отработало хорошо</p>',
        trigger_rule=TriggerRule.ALL_SUCCESS
    )

    postgres >> spark_pi >> email

sample_dag()
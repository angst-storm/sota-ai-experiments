repo:
	helm repo add airflow-stable https://airflow-helm.github.io/charts
	helm repo update

install: 
	helm install airflow airflow-stable/airflow --namespace=airflow --create-namespace --version=8.9.0 --values=values.yaml --wait

ui:
	kubectl port-forward svc/airflow-web 8080:8080 --namespace airflow

upgrade:
	helm upgrade airflow airflow-stable/airflow --namespace=airflow --version=8.9.0 --values=values.yaml --wait

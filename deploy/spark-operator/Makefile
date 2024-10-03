repo:
	helm repo add spark-operator https://kubeflow.github.io/spark-operator
	helm repo update

install:
	helm install spark-operator spark-operator/spark-operator --namespace=spark-operator --create-namespace --values=values.yaml --version=1.1.27 --wait

upgrade:
	helm upgrade spark-operator spark-operator/spark-operator --namespace=spark-operator --values=values.yaml --version=1.1.27 --wait

roles:
	kubectl delete serviceaccount spark -n spark-operator
	kubectl delete clusterrolebinding spark-role -n spark-operator

sparkapp:
	kubectl apply -f ../sparkapp/sparkapp.yaml

kind-cluster:
	kind create cluster --name sota

destroy-kind-cluster:
	kind delete cluster --name sota

build:
	docker build . -f deploy/airflow/Dockerfile -t customairflow:7

load:
	kind load docker-image customairflow:7 --name sota
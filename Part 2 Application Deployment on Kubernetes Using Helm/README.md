# Kubernetes Application Deployment with Monitoring
Welcome to this interactive guide! This project demonstrates how to deploy a sample application using Helm charts on a Kubernetes cluster (Minikube) and implement basic monitoring with Prometheus and Grafana.

## Project Objectives
Deploy an application on a local Kubernetes cluster using Helm charts.
Expose the application locally for easy access.
Implement basic monitoring using Prometheus and Grafana to monitor application health and performance.
##  Prerequisites
Before starting, ensure you have the following installed on your system:

Minikube
Start a lightweight Kubernetes cluster locally.
Kubectl
CLI tool to interact with Kubernetes clusters.
Helm
A package manager for Kubernetes.
Docker Desktop (Optional)
Needed for running containers locally.
Verify installations:

```bash
minikube version
kubectl version --client
helm version
```
## Step 1: Set Up Kubernetes
Choose a local Kubernetes environment like Minikube or Kind.

Minikube Setup:
Install Minikube
```bash
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
```

Start Minikube

```bash
minikube start --driver=docker
```

Enable Ingress Controller
```bash
minikube addons enable ingress
```

## Step 2: Install Helm

Install Helm
```bash
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 
```

Verify Helm installation
```bash
 helm version
```
## Step 3: Create a Helm Chart
Generate a Helm chart for your application:

Create a new Helm chart
```bash
helm create myapp
```
Navigate to the chart directory
```bash
cd myapp
```

Deploy the application
## Step 5: Deploy the Application
Install Helm Chart:

Deploy the application
```bash
helm install myapp ./myapp
```
Verify deployment
```bash
kubectl get pods
kubectl get svc
```
Expose the Application:

Access via Minikube (if using Minikube)
```bash
minikube service myapp
```
## Step 6: Add Monitoring
Install Prometheus and Grafana Using Helm:

Add Prometheus Helm repo
```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
```

Install Prometheus
```bash
helm install prometheus prometheus-community/prometheus
```

Add Grafana Helm repo
```bash
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update
```

Install Grafana
```bash
helm install grafana grafana/grafana --set adminPassword=admin
```
Access Grafana:
Get Grafana service details
```bash
kubectl get svc --namespace default grafana
```

Port-forward Grafana to access it locally
```bash
kubectl port-forward svc/grafana 3000:80
```
Visit http://localhost:3000, and log in with:

Username: admin
Password: admin
## Configure Grafana
Add Prometheus as a data source:

Navigate to Configuration > Data Sources in Grafana.
Select Prometheus and enter the Prometheus service URL (e.g., http://prometheus-server).
Import Kubernetes dashboards:

Go to Dashboard > Import in Grafana.
Use a dashboard ID like 3119 (Kubernetes cluster monitoring).

## Step 7: Test and Validate
Open the application in your browser (via Minikube service).
Access Grafana to view application and cluster metrics.
Ensure metrics like CPU usage, memory, and request rates are visible.


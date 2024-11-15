# Deploy the application
helm install myapp ./myapp

# Verify deployment
kubectl get pods
kubectl get svc

#Expose the Application

# Access via Minikube (if using Minikube)
minikube service myapp
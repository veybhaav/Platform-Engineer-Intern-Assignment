# Platform-Engineer-Intern-Assignment

# Part- 1: Infrastructure Deployment Using Terraform

## Objectives

- Deploy AWS services using **Terraform** or a local alternative such as **LocalStack**.
- Develop an application in any language that utilizes the deployed AWS services.
- Ensure the application interacts with these services and can be accessed locally.

---

## Functional Requirements

1. Deploy AWS services using Terraform:
   - **S3**: For file storage and retrieval.
   - **SQS**: For sending and receiving messages.
   - **Secrets Manager**: For securely managing sensitive information.
   - **EC2**: For hosting or integrating the application.

2. Develop an application that:
   - Interacts with **SQS** by sending and receiving messages.
   - Uploads and retrieves files from **S3**.
   - Accesses secrets stored in **Secrets Manager**.
   - Is hosted on or interacts with an **EC2 instance**.

---

## Infrastructure Setup

### AWS Services Deployed
- **S3 (Simple Storage Service)**: Provides scalable object storage.
- **SQS (Simple Queue Service)**: Manages message queues for communication between services.
- **Secrets Manager**: Secures sensitive information like credentials.
- **EC2 (Elastic Compute Cloud)**: Provides virtual servers for running applications.

---

## Application Development

- The application interacts with all deployed AWS services:
  1. **SQS**: Demonstrates queue functionality by sending and receiving messages.
  2. **S3**: Handles file uploads and downloads.
  3. **Secrets Manager**: Securely retrieves stored secrets.
  4. **EC2**: Hosts the application or acts as an infrastructure component.
  
- The application can be written in any language, such as Python, Go, or Node.js.

---

## Deliverables

### Terraform Deliverables
1. Modular Terraform configuration for all AWS services.
2. Proper state management for tracking resource changes.

### Application Deliverables
1. Source code for the application.
2. Instructions for running the application locally and connecting it to AWS services.

---

# Application Deployment on Kubernetes Using Helm

## Objectives

- Deploy an application on a Kubernetes cluster using **Helm charts**.
- Implement **basic monitoring** for the deployed application.
- Ensure the application is accessible locally via the Kubernetes cluster.

---

## Functional Requirements

1. Set up a Kubernetes cluster using tools like **Minikube** or **Kind**.
2. Configure and use **Helm charts** to deploy the application.
3. Expose the application locally via Kubernetes services such as **NodePort** or **Ingress**.
4. Implement basic monitoring to gather insights into the application’s health and performance.

---

## Kubernetes Setup

### Prerequisites
1. Install **kubectl**: [Install kubectl](https://kubernetes.io/docs/tasks/tools/)
2. Install a local Kubernetes environment:
   - **Minikube**: [Minikube Installation Guide](https://minikube.sigs.k8s.io/docs/start/)
   - **Kind**: [Kind Installation Guide](https://kind.sigs.k8s.io/docs/user/quick-start/)
3. Install **Helm**: [Helm Installation Guide](https://helm.sh/docs/intro/install/)

---


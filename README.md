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

# Part -2 : Application Deployment on Kubernetes Using Helm

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
# Comprehensive Solution: Application and Infrastructure Deployment

## Deliverables

### 1. **Source Code**
Host all source code in a Git repository (e.g., GitHub, GitLab).  
**Repository Contents:**
- **Application Code:** The full application implementation in the chosen language.
- **Terraform Scripts:** Scripts to provision AWS infrastructure.
- **Helm Charts:** YAML files to deploy the application on a Kubernetes cluster.
- **Monitoring Configuration:** Setup files for monitoring tools like Prometheus and Grafana.
- **Documentation:** Accompanying documentation files.

### 2. **Documentation**

#### **README.md**
A single point of reference for developers to set up and run the project.  
Includes:
1. **Setting Up Locally:**
   - Step-by-step guide for setting up the environment, tools, and dependencies.
   - Instructions for deploying the infrastructure using Terraform or LocalStack.
   - Guidelines for deploying the application on Kubernetes using Helm.
   - Explanation of the monitoring setup and how to view metrics.
   
2. **Configuring and Running:**
   - How to configure variables like bucket names, queue names, etc.
   - Running the application and verifying its functionality.
   
3. **Sample Commands:**
   - Terraform: `terraform apply`
   - Helm: `helm install my-app ./my-app`

#### **Technical Documentation**
A deeper dive into the architecture and design decisions.  
**Contents:**
- **System Overview:** High-level explanation of the system’s purpose and components.
- **Architecture Diagram:** Visual depiction of the interaction between components like S3, SQS, EC2, Kubernetes, etc.
- **Design Decisions:** Justification for using tools like Terraform, Helm, and Prometheus.
- **Assumptions and Dependencies:**
  - Use of LocalStack for local deployment.
  - Assumes Docker and Kubernetes are pre-installed.

---

### 3. **Test Cases**
**Testing Guidelines:**
1. **Infrastructure Testing:**
   - Validate Terraform plans using `terraform plan`.
   - Test resource provisioning by verifying the state file and LocalStack dashboard.
   
2. **Application Testing:**
   - Test SQS functionality by sending and receiving sample messages.
   - Verify S3 data upload and retrieval using application endpoints.
   - Confirm secret access from Secrets Manager in application logs.

**Sample Test Scripts:**
- A Python script for sending test messages to the SQS queue.
- Bash commands for validating the presence of S3 buckets.

---

### 4. **Monitoring Configuration**
A brief overview of the monitoring setup and any configured alerts.  
**Contents:**
- **Monitoring Tools:**
  - Prometheus: Scrapes metrics from Kubernetes and application.
  - Grafana: Visualizes metrics and sets up dashboards.
  
- **Thresholds and Alerts:**
  - CPU/Memory usage thresholds for Kubernetes pods.
  - Alerts for queue depth in SQS or high error rates in the application.

---



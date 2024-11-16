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

## Deployment Instructions

### Pre-requisites
- Install **Terraform**: [Terraform Installation Guide](https://www.terraform.io/downloads)
- Install **AWS CLI** or **LocalStack** for emulating AWS services:  
  - [AWS CLI Installation Guide](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)  
  - [LocalStack Installation Guide](https://docs.localstack.cloud/get-started/)
- Configure AWS credentials:
  ```bash
  aws configure

# Part - 1: AWS Infrastructure Deployment with Terraform and Application Interaction

This repository contains code and instructions to provision AWS infrastructure using Terraform and deploy a Python application that interacts with the provisioned services. The project supports deployment on **AWS** or **LocalStack** (a local AWS testing environment).

## Objectives

This project aims to:

- Deploy AWS services using Terraform, with support for **AWS** or **LocalStack** (local testing environment).
- Develop a local application that interacts with these deployed services.
- Ensure the application is functional and demonstrates interaction with AWS services.

## Functional Requirements

1. Deploy the following AWS services using Terraform:
   - **S3**: For file storage.
   - **SQS**: For sending and receiving messages.
   - **Secrets Manager**: For securely managing sensitive data.
   - **EC2**: For hosting or integrating the application.
2. Develop an application in your preferred language (e.g., Python, Go, Node.js) to:
   - Send and receive messages via SQS.
   - Upload and retrieve files from S3.
   - Access sensitive data securely from Secrets Manager.
   - Utilize EC2 for hosting or integration.

---

## Infrastructure Setup

### AWS Services Provisioned
- **S3**: Bucket for storing and retrieving files.
- **SQS**: Queue for messaging.
- **Secrets Manager**: Secure storage for sensitive information.
- **EC2**: Virtual server for hosting the application.

### Tools and Technologies
- **Terraform**: Infrastructure as Code for resource provisioning.
- **AWS CLI** or **LocalStack**: To manage AWS resources or emulate AWS services locally.
- **Python** (or your preferred language): For application development.

---

## Application Development

The application demonstrates:
- **SQS**: Sending and receiving messages.
- **S3**: Uploading and downloading files.
- **Secrets Manager**: Securely retrieving stored secrets.
- **EC2**: Hosting or interacting with the application.

The application is designed to work both locally and with AWS/LocalStack.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Pre-requisites](#pre-requisites)
- [Setup Instructions](#setup-instructions)
  - [Step 1: Clone the Repository](#step-1-clone-the-repository)
  - [Step 2: Install Dependencies](#step-2-install-dependencies)
  - [Step 3: Configure AWS or LocalStack](#step-3-configure-aws-or-localstack)
- [Deploying Infrastructure](#deploying-infrastructure)
- [Running the Application](#running-the-application)
- [Clean-Up](#clean-up)
- [FAQ](#faq)
- [Contributing](#contributing)



## Overview

The project provisions the following AWS resources:
- **S3**: For storing files.
- **SQS**: For sending and receiving messages.
- **Secrets Manager**: For securely managing sensitive data.
- **EC2**: A virtual server for running the application.

The included Python application interacts with these services, demonstrating:
- Uploading and downloading files from S3.
- Sending and receiving messages from SQS.
- Retrieving secrets from Secrets Manager.

---

## Features

1. **Infrastructure as Code**: Uses Terraform for automated provisioning.
2. **Flexible Deployment**: Supports both AWS and LocalStack.
3. **Modular Design**: Reusable and clean Terraform code.
4. **Interactive Application**: Python app showcases real-world AWS interactions.

---

## Pre-requisites

### Tools and Accounts
- **Terraform**: [Download](https://www.terraform.io/downloads)
- **AWS CLI**: [Install](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)
- **Python**: Version 3.8 or higher
- **LocalStack** (optional): For local testing ([Install](https://docs.localstack.cloud/get-started/))  

### Python Dependencies
Install the required libraries:
```bash
pip install boto3
```
LocalStack (for local option): Install using Docker:
```bash
pip install localstack
```

AWS Permissions
Ensure your IAM user or role has permissions for:

S3, SQS, Secrets Manager, EC2.

## Project Setup
Step 1: Clone the Repository
Clone this project to your local machine:

```bash
git clone https://github.com/your-repository/aws-terraform-app.git
cd aws-terraform-app
```
Step 2: Install Terraform
Verify Terraform installation:
```bash
terraform --version
```
If not installed, follow the official Terraform Installation Guide.

Step 3: Configure AWS or LocalStack
Option 1: AWS Cloud Setup
Configure your AWS CLI:
aws configure
Provide:

Access Key
Secret Key
Region (e.g., us-east-1)
Option 2: LocalStack Setup
Run LocalStack in a Docker container:
```bash
localstack start
```
Add the following to provider.tf:


provider "aws" {
  region      = "us-east-1"
  endpoint    = "http://localhost:4566" # LocalStack endpoint
  access_key  = "mock_key"
  secret_key  = "mock_secret"
}

## Deploy Infrastructure
Initialize Terraform
Run the following to download necessary providers and modules:

```bash
terraform init
```
Validate Configuration
Validate your Terraform files:
```bash
terraform validate
```
Provision Resources
Apply the configuration:
```bash
terraform apply -auto-approve
```
Terraform will output the following:
S3 bucket name
SQS queue URL
Secret ARN
EC2 instance ID
Run the Application
Set Environment Variables
Export Terraform outputs as environment variables:

```bash
export S3_BUCKET_NAME="<s3_bucket_name>"
export SQS_QUEUE_URL="<sqs_queue_url>"
export SECRET_NAME="<secret_name>"
```
Run the Python Application
Navigate to the app directory and run the script:
```
cd app
python app.py
```
Expected Outputs

S3: File uploaded and downloaded.
SQS: Message sent and received.
Secrets Manager: Secret value retrieved.
Clean Up
To delete all provisioned resources, run:
```
terraform destroy -auto-approve
```
## FAQs
Can I test this project without AWS credentials?
Yes, use LocalStack for local testing.

What if Terraform commands fail?
Ensure:

Correct Terraform syntax (terraform validate).
AWS CLI or LocalStack is configured.
How can I extend this project?
Add additional AWS services or enhance the Python app.

## Contributing
Feel free to fork this repository and create pull requests for improvements.

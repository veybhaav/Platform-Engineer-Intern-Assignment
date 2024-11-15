# AWS Infrastructure Deployment with Terraform and Application Interaction

This repository contains code and instructions to provision AWS infrastructure using Terraform and deploy a Python application that interacts with the provisioned services. The project supports deployment on **AWS** or **LocalStack** (a local AWS testing environment).

---

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

---

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

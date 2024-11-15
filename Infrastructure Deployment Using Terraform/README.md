# AWS Infrastructure Deployment with Terraform and Application Interaction (Local or Cloud)
This project guides you to provision AWS infrastructure using Terraform and develop a simple Python application that interacts with the deployed services. It is designed to work with AWS directly or with LocalStack for local testing.

## Table of Contents
Overview
Project Features
Pre-requisites
Project Setup
Step 1: Clone the Repository
Step 2: Install Terraform
Step 3: Configure AWS or LocalStack
Deploy Infrastructure
Run the Application
Clean Up
FAQs
Contributing
## Overview
This project provisions the following AWS resources:

S3 (Simple Storage Service): For storing files.
SQS (Simple Queue Service): For sending and receiving messages.
Secrets Manager: For securely storing sensitive information.
EC2 Instance: A virtual server for running the application.
A Python application is included to interact with these services. The app:

Uploads and downloads files from S3.
Sends and retrieves messages from SQS.
Reads secrets from Secrets Manager.
## Project Features
Infrastructure as Code (IaC): Uses Terraform for AWS provisioning.
Cloud and Local Options: Supports deployment on AWS or locally via LocalStack.
Interactive Application: A Python app showcasing service interaction.
Modular Terraform Configuration: Clean, reusable module-based Terraform code.
## Pre-requisites
Tools and Accounts
Terraform: Download and install Terraform.
AWS CLI (for AWS option): Install and configure using AWS CLI setup guide.
LocalStack (for local option): Install using Docker:
```bash
pip install localstack
```
Python: Install Python (≥3.8) and the boto3 library:
```bash
pip install boto3
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

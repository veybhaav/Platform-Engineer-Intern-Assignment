import boto3
import json
import os

# Initialize boto3 clients
s3 = boto3.client('s3')
sqs = boto3.client('sqs')
secretsmanager = boto3.client('secretsmanager')

# S3 interaction
def upload_to_s3(bucket_name, file_name, data):
    s3.put_object(Bucket=bucket_name, Key=file_name, Body=data)
    print(f"Uploaded {file_name} to {bucket_name}.")

def download_from_s3(bucket_name, file_name):
    response = s3.get_object(Bucket=bucket_name, Key=file_name)
    data = response['Body'].read().decode('utf-8')
    print(f"Downloaded {file_name} from {bucket_name}: {data}")

# SQS interaction
def send_sqs_message(queue_url, message_body):
    sqs.send_message(QueueUrl=queue_url, MessageBody=message_body)
    print(f"Sent message to queue {queue_url}.")

def receive_sqs_message(queue_url):
    response = sqs.receive_message(QueueUrl=queue_url, MaxNumberOfMessages=1)
    if 'Messages' in response:
        message = response['Messages'][0]
        print(f"Received message: {message['Body']}")
        sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=message['ReceiptHandle'])

# Secrets Manager interaction
def get_secret(secret_name):
    response = secretsmanager.get_secret_value(SecretId=secret_name)
    secret = json.loads(response['SecretString'])
    print(f"Retrieved secret: {secret}")

# Run all operations
if __name__ == "__main__":
    bucket_name = os.getenv("S3_BUCKET_NAME")
    queue_url = os.getenv("SQS_QUEUE_URL")
    secret_name = os.getenv("SECRET_NAME")

    upload_to_s3(bucket_name, "test.txt", "Hello, World!")
    download_from_s3(bucket_name, "test.txt")
    send_sqs_message(queue_url, "Hello from SQS!")
    receive_sqs_message(queue_url)
    get_secret(secret_name)

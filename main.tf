module "s3" {
  source = "./modules/s3"
  s3_bucket_name = var.s3_bucket_name
}

module "sqs" {
  source = "./modules/sqs"
  queue_name = var.queue_name
}

module "secrets_manager" {
  source = "./modules/secrets_manager"
  secret_name = var.secret_name
  secret_value = var.secret_value
}

module "ec2" {
  source = "./modules/ec2"
  instance_type = var.instance_type
  ami_id = var.ami_id
}

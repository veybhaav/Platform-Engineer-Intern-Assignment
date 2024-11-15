variable "s3_bucket_name" { type = string }
variable "queue_name" { type = string }
variable "secret_name" { type = string }
variable "secret_value" { type = string }
variable "instance_type" { default = "t2.micro" }
variable "ami_id" { type = string }

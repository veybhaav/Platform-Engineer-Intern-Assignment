resource "aws_sqs_queue" "example" {
  name = example-queue
}

output "sqs_queue_url" {
  value = aws_sqs_queue.example.url
}

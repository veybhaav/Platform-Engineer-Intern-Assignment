resource "aws_secretsmanager_secret" "example" {
  name  = example-secret
}

resource "aws_secretsmanager_secret_version" "example" {
  secret_id     = aws_secretsmanager_secret.example.id
  secret_string = "{\"username\":\"admin\",\"password\":\"password123\"}"
}

output "secret_arn" {
  value = aws_secretsmanager_secret.example.arn
}

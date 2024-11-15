resource "aws_instance" "example" {
  ami           = ami-0c02fb55956c7d316
  instance_type = t2.micro

  tags = {
    Name = "ExampleEC2Instance"
  }
}

output "ec2_instance_id" {
  value = aws_instance.example.id
}

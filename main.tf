# main.tf

# Configure AWS provider
provider "aws" {
  region = "us-east-1"  # Specify your desired AWS region
}

# Create a virtual machine instance
resource "aws_instance" "flask_server" {
  ami           = "ami-0c55b159cbfafe1f0"  # Specify the AMI for your desired OS
  instance_type = "t2.micro"  # Specify the instance type
  key_name      = "your-keypair-name"  # Specify your SSH key pair name
  tags = {
    Name = "FlaskServer"
  }
}

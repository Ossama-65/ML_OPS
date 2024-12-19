resource "aws_instance" "mlops_server" {
  ami           = "ami-04505e74c0741db8d" # ID d'AMI (Ubuntu)
  instance_type = "t2.micro"
  key_name      = "mlops-key_ok" # Remplace par le nom de ta nouvelle clé

  tags = {
    Name = "mlops-end-to-end"
  }
}

resource "aws_s3_bucket" "mlflow_bucket" {
  bucket = "mlops-mlflow-bucket-${random_id.bucket_id.hex}"
}

resource "random_id" "bucket_id" {
  byte_length = 4
}

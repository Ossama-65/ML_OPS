output "instance_ip" {
  value = aws_instance.mlops_server.public_ip
}

output "mlflow_bucket_name" {
  value = aws_s3_bucket.mlflow_bucket.bucket
}

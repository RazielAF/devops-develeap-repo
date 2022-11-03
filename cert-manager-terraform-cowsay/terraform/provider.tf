provider "aws" {
  region = var.AWS_REGION
}

terraform {
  backend "s3" {
    bucket = "cowsay-state"
    key    = "cowsay-state"
    region = "eu-west-2"
  }
}

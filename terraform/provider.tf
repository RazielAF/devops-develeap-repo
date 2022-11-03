provider "aws" {
  region = var.AWS_REGION
}

terraform {
  backend "s3" {
    bucket = "mg-state"
    key    = "mg-state"
    region = "eu-west-2"
  }
}

subnets = {
  "a" = {
    cidr      = "10.0.0.0/24"
    az        = "eu-west-2a"
    public_ip = "true"
    tags = {
      Name = "maciejgroszyk_tf-public-subnet-1-eu-west-2b"
    }
  },
  "b" = {
    cidr      = "10.0.1.0/24"
    az        = "eu-west-2b"
    public_ip = "true"
    tags = {
      Name = "maciejgroszyk_tf-public-subnet-2-eu-west-2b"
    }
  }
}

aws_instances = {
  "a" = {
    ami           = "ami-0f540e9f488cfa27d"
    instance_type = "t2.micro"
    key_name      = "londonmaciejgroszyk"
    start_script  = "docker.sh"
    tags = {
      Name       = "maciejgroszyk_tf_ec2-1"
      created_by = "Maciej Groszyk"
      bootcamp   = "poland1"
    }
  },
  "b" = {
    ami           = "ami-0f540e9f488cfa27d"
    instance_type = "t2.micro"
    key_name      = "londonmaciejgroszyk"
    start_script  = "docker.sh"
    tags = {
      Name       = "maciejgroszyk_tf_ec2-2"
      created_by = "Maciej Groszyk"
      bootcamp   = "poland1"
    }
  }
}
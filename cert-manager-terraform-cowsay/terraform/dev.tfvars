
aws_instance_config = {
  ami           = "ami-0f540e9f488cfa27d"
  instance_type = "t2.micro"
  key_name      = "londonmaciejgroszyk"
  start_script  = "modules/compute/docker.sh"
  tags = {
    Name       = "dev-maciejgroszyk_tf_ec2"
    created_by = "Maciej Groszyk"
    bootcamp   = "poland1"
  }
}

subnets = [
  {
    cidr      = "10.0.0.0/24"
    az        = "eu-west-2a"
    public_ip = "true"
    tags = {
      Name = "dev-maciejgroszyk_tf-public-subnet-1-eu-west-2b"
    }
  }
]

volume_tags = {
  created_by = "Maciej Groszyk"
  bootcamp   = "poland1"
}

route_table = {
  Name = "maciejgroszyk_tf_crt"
  cidr = "0.0.0.0/0"
}

internet_gateway_tags = {
  Name = "maciejgroszyk_tf_igw"
}

ingress_cidr_blocks = ["0.0.0.0/0"]

ingress_rules = ["22", "80", "8080"]

egress_cidr_blocks = ["0.0.0.0/0"]

egress_rule = ["0"]

rules = {
  "22"   = [22, 22, "tcp"] 
  "80"   = [80, 80, "tcp"]
  "8080" = [8080, 8080, "tcp"]
  "0"    = [0, 0, "all"] 
}

security_group_tag = {
  Name = "mg_security_group_tf"
}

tf_vpc = {
  cidr_block           = "10.0.0.0/16"
  enable_dns_support   = "true"
  enable_dns_hostnames = "true"
  instance_tenancy     = "default"
  tags = {
    Name = "dev-maciejgroszyk_tf_vpc"
  }
}

health_check_interval = 10
health_check_timeout  = 5

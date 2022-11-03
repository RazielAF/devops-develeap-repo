locals {
  subnets_ids        = ["${aws_subnet.subnets["a"].id}", "${aws_subnet.subnets["b"].id}"]
  security_group_ids = ["${aws_security_group.mg_security_group_tf.id}"]
}

variable "AWS_REGION" {
  default = "eu-west-2"
}

variable "volume_tags" {
  type = map(any)
  default = {
    created_by = "Maciej Groszyk"
    bootcamp   = "poland1"
  }
}

variable "route_table" {
  type = map(any)
  default = {
    Name = "maciejgroszyk_tf_crt"
    cidr = "0.0.0.0/0"
  }
}

variable "internet_gateway_tags" {
  type = map(any)
  default = {
    Name = "maciejgroszyk_tf_igw"
  }
}
variable "ingress_cidr_blocks" {
  type    = list(string)
  default = ["0.0.0.0/0"]
}
variable "ingress_rules" {
  type    = list(string)
  default = ["22", "80", "8080"]
}
variable "egress_cidr_blocks" {
  type    = list(string)
  default = ["0.0.0.0/0"]
}

variable "egress_rules" {
  type    = list(string)
  default = ["0"]
}
variable "rules" {
  type = any
  #   type = map(list(object({
  #     from_port = number,
  #     to_port   = number,
  #     protocol  = string,
  #   })))
  default = {
    "22"   = [22, 22, "tcp"]
    "80"   = [80, 80, "tcp"]
    "8080" = [8080, 8080, "tcp"]
    "0"    = [0, 0, "all"]
  }
}

variable "security_group_tag" {
  type = map(any)
  default = {
    Name = "mg_security_group_tf"
  }
}

variable "aws_instances" {
  type = map(object({
    ami           = string
    instance_type = string
    start_script  = string
    tags          = map(any)
    key_name      = string
  }))
  description = "AWS instances"
}

variable "subnets" {
  type = map(object({
    cidr      = string
    az        = string
    tags      = map(any)
    public_ip = bool
  }))
}

variable "lb_name" {
  type    = string
  default = "maciejgroszyk-tf-alb"
}

variable "lb_type" {
  type    = string
  default = "application"
}

variable "alb_listener" {
  type = map(string)
  default = {
    port                = "80"
    protocol            = "HTTP"
    default_action_type = "forward"
  }
}

variable "mg_target_group" {
  type = any
  default = {
    name     = "maciejgroszyk-tg-alb"
    port     = 80
    protocol = "HTTP"
  }
}

variable "attach_port" {
  type    = number
  default = 8080
}

variable "tf_vpc" {
  type = any
  default = {
    cidr_block           = "10.0.0.0/16"
    enable_dns_support   = "true"
    enable_dns_hostnames = "true"
    instance_tenancy     = "default"
    tags = {
      Name = "maciejgroszyk_tf_vpc"
    }
  }
}
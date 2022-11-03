resource "aws_instance" "maciejgroszyk_tf_ec2" {
  count                  = 1
  ami                    = var.aws_instance_config["ami"]
  instance_type          = var.aws_instance_config["instance_type"]
  iam_instance_profile   = "maciekG_role" #TODO
  subnet_id              = var.subnets_list[0]
  tags                   = var.aws_instance_config["tags"]
  user_data              = file(var.aws_instance_config["start_script"])
  volume_tags            = var.volume_tags
  vpc_security_group_ids = [var.security_group_id]
  key_name               = var.aws_instance_config["key_name"]
}

# resource "null_resource" "copy_file" {

#   provisioner "file" {
#     source      = "../docker-compose-prod.yaml"
#     destination = "/home/ubuntu/docker-compose.yaml"
#   }

#   connection {
#     type        = "ssh"
#     host        = aws_instance.maciejgroszyk_tf_ec2[0].public_ip
#     user        = "ubuntu"
#     # private_key = file("/home/jenkins/ssh/londonmaciejgroszyk.pem")
#     private_key = file("/home/mac/Downloads/londonmaciejgroszyk.pem")
  
#   }

#   depends_on = [aws_instance.maciejgroszyk_tf_ec2[0]]

# }
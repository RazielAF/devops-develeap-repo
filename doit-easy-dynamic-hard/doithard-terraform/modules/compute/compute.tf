resource "aws_instance" "maciejgroszyk_tf_ec2" {
  count                  = var.single_config == false ? 2:1
  ami                    = var.aws_instance_config["ami"]
  instance_type          = var.aws_instance_config["instance_type"]
  subnet_id              = var.subnets_list[0]
  tags                   = var.aws_instance_config["tags"]
  user_data              = file(var.aws_instance_config["start_script"])
  volume_tags            = var.volume_tags
  vpc_security_group_ids = [var.security_group_id]
  key_name               = var.aws_instance_config["key_name"]
}
 
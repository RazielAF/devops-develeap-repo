resource "aws_instance" "maciejgroszyk_tf_ec2" {
  for_each               = var.aws_instances
  ami                    = each.value.ami
  instance_type          = each.value.instance_type
  subnet_id              = aws_subnet.subnets["a"].id
  tags                   = each.value.tags
  user_data              = file(each.value.start_script)
  volume_tags            = var.volume_tags
  vpc_security_group_ids = [aws_security_group.mg_security_group_tf.id]
  key_name               = each.value.key_name
}
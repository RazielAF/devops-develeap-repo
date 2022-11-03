resource "aws_lb" "alb" {
  name               = var.lb_name
  load_balancer_type = var.lb_type
  subnets            = local.subnets_ids
  security_groups    = local.security_group_ids
}

resource "aws_lb_listener" "alb" {
  load_balancer_arn = aws_lb.alb.arn
  port              = var.alb_listener["port"]
  protocol          = var.alb_listener["protocol"]

  default_action {
    type             = var.alb_listener["default_action_type"]
    target_group_arn = aws_lb_target_group.mg-tf-target_group.arn
  }
}

resource "aws_lb_target_group" "mg-tf-target_group" {
  name     = var.mg_target_group["name"]
  port     = var.mg_target_group["port"]
  protocol = var.mg_target_group["protocol"]
  vpc_id   = aws_vpc.maciejgroszyk_tf_vpc.id

  health_check {
    port     = var.mg_target_group["port"]
    protocol = var.mg_target_group["protocol"]
    timeout  = 5
    interval = 10
  }
}

resource "aws_lb_target_group_attachment" "mg-attach" {
  for_each         = var.aws_instances
  target_group_arn = aws_lb_target_group.mg-tf-target_group.arn
  target_id        = aws_instance.maciejgroszyk_tf_ec2[each.key].id
  port             = var.attach_port
}

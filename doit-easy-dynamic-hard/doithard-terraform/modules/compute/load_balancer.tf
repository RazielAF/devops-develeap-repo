resource "aws_lb" "alb" {
  count = var.single_config == false ? 1:0
  name               = var.lb_name
  load_balancer_type = var.lb_type
  subnets            = var.subnets_list
  security_groups    = [var.security_group_id]
}

resource "aws_lb_listener" "alb" {
  count = var.single_config == false ? 1:0
  load_balancer_arn = aws_lb.alb[count.index].arn
  port              = var.alb_listener["port"]
  protocol          = var.alb_listener["protocol"]

  default_action {
    type             = var.alb_listener["default_action_type"]
    target_group_arn = aws_lb_target_group.mg-tf-target_group[count.index].arn
  }
}

resource "aws_lb_target_group" "mg-tf-target_group" {
  count = var.single_config == false ? 1:0
  name     = var.mg_target_group["name"]
  port     = var.mg_target_group["port"]
  protocol = var.mg_target_group["protocol"]
  vpc_id   = var.vpc_id

  health_check {
    port     = var.mg_target_group["port"]
    protocol = var.mg_target_group["protocol"]
    timeout  = var.health_check_timeout
    interval = var.health_check_interval
  }
}

resource "aws_lb_target_group_attachment" "mg-attach" {
  count            = var.single_config == false ? length(aws_instance.maciejgroszyk_tf_ec2):0
  target_group_arn = aws_lb_target_group.mg-tf-target_group[0].arn
  target_id        = aws_instance.maciejgroszyk_tf_ec2[count.index].id
  port             = var.attach_port
}



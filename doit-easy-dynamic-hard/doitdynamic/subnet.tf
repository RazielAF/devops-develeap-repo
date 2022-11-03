resource "aws_subnet" "subnets" {
  for_each                = var.subnets
  vpc_id                  = aws_vpc.maciejgroszyk_tf_vpc.id
  cidr_block              = each.value.cidr
  availability_zone       = each.value.az
  tags                    = each.value.tags
  map_public_ip_on_launch = each.value.public_ip
}
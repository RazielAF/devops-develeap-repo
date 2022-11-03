resource "aws_subnet" "maciejgroszyk_tf-public-subnet-1" {
    vpc_id = "${aws_vpc.maciejgroszyk_tf_vpc.id}"
    cidr_block = "10.0.0.0/24"
    map_public_ip_on_launch = "true"
    availability_zone = "eu-west-2a"
    tags = {
        Name = "maciejgroszyk_tf-public-subnet-1"
    }
}

resource "aws_subnet" "maciejgroszyk_tf-public-subnet-2" {
    vpc_id = "${aws_vpc.maciejgroszyk_tf_vpc.id}"
    cidr_block = "10.0.1.0/24"
    map_public_ip_on_launch = "true"
    availability_zone = "eu-west-2b"
    tags = {
        Name = "maciejgroszyk_tf-public-subnet-2"
    }
}
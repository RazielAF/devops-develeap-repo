resource "aws_internet_gateway" "maciejgroszyk_tf_igw" {
    vpc_id = "${aws_vpc.maciejgroszyk_tf_vpc.id}"
    tags = {
	Name = "maciejgroszyk_tf_igw"
    }
}

resource "aws_route_table" "maciejgroszyk_tf_crt" {
    vpc_id = "${aws_vpc.maciejgroszyk_tf_vpc.id}"
    route {
	cidr_block = "0.0.0.0/0"
  	gateway_id = "${aws_internet_gateway.maciejgroszyk_tf_igw.id}"
    }
    tags = {
	Name = "maciejgroszyk_tf_crt"
    }
}

resource "aws_route_table_association" "mg_crta_public_subnet-1" {
    subnet_id = "${aws_subnet.maciejgroszyk_tf-public-subnet-1.id}"
    route_table_id = "${aws_route_table.maciejgroszyk_tf_crt.id}"
}

resource "aws_route_table_association" "mg_crta_public_subnet-2" {
    subnet_id = "${aws_subnet.maciejgroszyk_tf-public-subnet-2.id}"
    route_table_id = "${aws_route_table.maciejgroszyk_tf_crt.id}"
}

resource "aws_security_group" "mg_security_group_tf" {
    vpc_id = "${aws_vpc.maciejgroszyk_tf_vpc.id}"

    egress {
        from_port = 0
        to_port = 0
        protocol = -1
        cidr_blocks = ["0.0.0.0/0"]
    }
    ingress {
        from_port = 22
        to_port = 22
        protocol = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }
    ingress {
        from_port = 8080
        to_port = 8080
        protocol = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }
    tags = {
        Name = "mg_security_group_tf"
    }
}

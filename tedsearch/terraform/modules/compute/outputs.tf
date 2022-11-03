output "public_ip"{
    description = "public ip"
    value = aws_instance.maciejgroszyk_tf_ec2[0].public_ip  
}
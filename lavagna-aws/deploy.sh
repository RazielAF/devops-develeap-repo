if [ -z "$1" ]; then
    echo "Pls add a tag!"
    echo "last package:"
    ls | grep "lavagna" | tail -1
    exit 0;
fi
ssh -i ~/Downloads/londonmaciejgroszyk.pem ubuntu@ec2-18-130-192-36.eu-west-2.compute.amazonaws.com "rm -rf *"
scp -i ~/Downloads/londonmaciejgroszyk.pem lavagna-startup-package_$1.tar.gz ubuntu@ec2-18-130-192-36.eu-west-2.compute.amazonaws.com:~/lavagna-startup-package_$1.tar.gz
ssh -i ~/Downloads/londonmaciejgroszyk.pem ubuntu@ec2-18-130-192-36.eu-west-2.compute.amazonaws.com "aws ecr get-login-password --region eu-west-2 | docker login --username AWS --password-stdin 644435390668.dkr.ecr.eu-west-2.amazonaws.com"
# docker-compose down; \
# docker rm -f $(docker ps -aq); \
# docker pull 644435390668.dkr.ecr.eu-west-2.amazonaws.com/maciejgroszyklavagna:$1; \
# docker tag 644435390668.dkr.ecr.eu-west-2.amazonaws.com/maciejgroszyklavagna:$1 644435390668.dkr.ecr.eu-west-2.amazonaws.com/maciejgroszyklavagna:latest; \
# tar xzf lavagna-startup-package_$1.tar.gz;
# docker-compose up;"
ssh -i ~/Downloads/londonmaciejgroszyk.pem ubuntu@ec2-18-130-192-36.eu-west-2.compute.amazonaws.com "docker-compose down"
ssh -i ~/Downloads/londonmaciejgroszyk.pem ubuntu@ec2-18-130-192-36.eu-west-2.compute.amazonaws.com "docker rm -f $(docker ps -aq)"
ssh -i ~/Downloads/londonmaciejgroszyk.pem ubuntu@ec2-18-130-192-36.eu-west-2.compute.amazonaws.com "docker system prune -af"
ssh -i ~/Downloads/londonmaciejgroszyk.pem ubuntu@ec2-18-130-192-36.eu-west-2.compute.amazonaws.com "docker pull 644435390668.dkr.ecr.eu-west-2.amazonaws.com/maciejgroszyklavagna:$1"
ssh -i ~/Downloads/londonmaciejgroszyk.pem ubuntu@ec2-18-130-192-36.eu-west-2.compute.amazonaws.com "docker tag 644435390668.dkr.ecr.eu-west-2.amazonaws.com/maciejgroszyklavagna:$1 644435390668.dkr.ecr.eu-west-2.amazonaws.com/maciejgroszyklavagna:latest "
ssh -i ~/Downloads/londonmaciejgroszyk.pem ubuntu@ec2-18-130-192-36.eu-west-2.compute.amazonaws.com "tar xzf lavagna-startup-package_$1.tar.gz"
ssh -i ~/Downloads/londonmaciejgroszyk.pem ubuntu@ec2-18-130-192-36.eu-west-2.compute.amazonaws.com "docker-compose up"

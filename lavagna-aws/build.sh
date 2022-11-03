if [ -z "$1" ]; then
    echo "Pls add a tag!"
    echo "last package:"
    ls | grep "lavagna" | tail -1
    exit 1;
fi
docker build -t maciejgroszyklavagna:$1 .
tar -zcvf lavagna-startup-package_$1.tar.gz conf/ docker-compose.yaml maven-data/
aws ecr get-login-password --region eu-west-2 | docker login --username AWS --password-stdin 644435390668.dkr.ecr.eu-west-2.amazonaws.com
docker tag maciejgroszyklavagna:$1 644435390668.dkr.ecr.eu-west-2.amazonaws.com/maciejgroszyklavagna:$1
docker push 644435390668.dkr.ecr.eu-west-2.amazonaws.com/maciejgroszyklavagna:$1
exit 0; 
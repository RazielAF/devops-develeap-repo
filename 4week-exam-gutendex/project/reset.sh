docker rm -f $(docker ps -aq)
docker rmi project_gutendex_app
docker-compose down
docker-compose up
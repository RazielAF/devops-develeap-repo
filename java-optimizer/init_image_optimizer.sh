#!/bin/bash

docker build -t image_optimizer .
echo it is in dir $1
echo it is out dir $2
docker run -itdv "$1":/app/in -v "$2":/app/out image_optimizer 

#!/bin/bash

docker build -t cowsay_image .

if [ "$1" == "" ];then
EXTERNAL_PORT=8081
else
EXTERNAL_PORT=$1
fi

docker run -d -p $EXTERNAL_PORT:8080 cowsay_image $EXTERNAL_PORT

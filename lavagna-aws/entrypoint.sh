#!/bin/sh
java -Xms64m -Xmx128m -Ddatasource.dialect="MYSQL" \
-Ddatasource.url="jdbc:mysql://maciejgroszykdb.cn4zjh0zairt.eu-west-2.rds.amazonaws.com:3306/lavagna?useUnicode=true&characterEncoding=utf-8&useSSL=false" \
-Ddatasource.username="admin" \
-Ddatasource.password="fk6teGkrarZ26jsG" \
-Dspring.profiles.active="dev" \
-jar lavagna-jetty-console.war --headless
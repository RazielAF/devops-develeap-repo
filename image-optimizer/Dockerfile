FROM maven:3.5-jdk-8 AS build  
WORKDIR /app
COPY /src ./src  
COPY pom.xml .  
COPY entrypoint.sh .
RUN mvn package
COPY target/deps/pngtastic-1.0.jar target/deps/
ENTRYPOINT java -cp target/deps/pnggastic-1.0.jar -jar target/image-web-optimizer-0.0.2-SNAPSHOT.jar in/ out/

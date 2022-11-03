FROM maven:3.6.2-jdk-8
WORKDIR /app
# COPY target/embedash-1.1-SNAPSHOT.jar target/embedash-1.1-SNAPSHOT.jar
COPY . .
ENTRYPOINT ["java", "-jar", "target/embedash-1.1-SNAPSHOT.jar"]
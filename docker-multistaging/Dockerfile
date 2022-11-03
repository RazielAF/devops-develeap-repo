FROM maven:3.5-jdk-8 AS build  
WORKDIR app/
COPY src/ src/ 
COPY pom.xml .
ENTRYPOINT ["/bin/sh"]
RUN mvn verify

FROM adoptopenjdk/openjdk8:alpine-jre
WORKDIR app/
COPY --from=build app/target/hello-java.jar .
ENTRYPOINT ["java", "-jar", "hello-java.jar"]


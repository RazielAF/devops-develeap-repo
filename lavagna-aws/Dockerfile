FROM maven:3.8.6-jdk-8 AS build
WORKDIR project
COPY src/ src/
COPY pom.xml .
COPY LICENSE-GPLv3.txt LICENSE-GPLv3.txt
RUN mvn verify

FROM adoptopenjdk/openjdk8:alpine-jre
WORKDIR project/
COPY --from=build project/target/lavagna-jetty-console.war  .
COPY entrypoint.sh entrypoint.sh 

ENTRYPOINT [ "sh", "entrypoint.sh" ]
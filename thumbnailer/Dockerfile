FROM maven:3.6.2-jdk-8
WORKDIR /thumbnailer
COPY . .
RUN mvn -f pom.xml verify
RUN cp thumbnail.sh target/thumbnail.sh
ENTRYPOINT ["entrypoint.sh"]


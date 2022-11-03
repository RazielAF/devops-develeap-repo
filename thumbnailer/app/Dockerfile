FROM maven:3.6.2-jdk-8
WORKDIR /app
COPY . .
RUN mvn verify
COPY thumbnail.sh target/thumbnail.sh
COPY entrypoint.sh target/entrypoint.sh
WORKDIR /app/target
RUN chmod 755 entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
CMD ["150"]
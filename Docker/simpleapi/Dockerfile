FROM openjdk:21-jdk-slim

WORKDIR /app

ENV APP_NAME=simpleapi \
    DB_HOST=172.18.0.2 \
    DB_NAME=springdb \
    DB_PORT=3306 \
    DB_USERNAME=root \
    DB_PASSWORD=password \
    SERVER_PORT=8787 

COPY target/simpleapi-0.0.1-SNAPSHOT.jar .

EXPOSE 8787

CMD ["java","-jar","simpleapi-0.0.1-SNAPSHOT.jar"]
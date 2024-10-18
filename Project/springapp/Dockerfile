# Build stage
ARG USER_GROUP="appuser"
 
FROM maven:3.8.5-openjdk-17 AS build
WORKDIR /app
COPY src ./src
COPY pom.xml .
 
RUN mvn clean package -DskipTests
 
# Runtime stage
FROM openjdk:17-jdk-slim
 
# Define the user and group to be created
ARG USER_GROUP
 
# Set the working directory
WORKDIR /app
 
# Create the user and group
RUN groupadd -r ${USER_GROUP} && useradd -r -g ${USER_GROUP} ${USER_GROUP}
 
# Copy the JAR file from the build stage
COPY --from=build /app/target/*.jar app.jar
 
# Set permissions for the jar file
RUN chown ${USER_GROUP}:${USER_GROUP} app.jar && chmod 500 app.jar
 
# Switch to the created user
USER ${USER_GROUP}
 
# Set the entrypoint for the container
ENTRYPOINT ["java", "-jar", "app.jar"]

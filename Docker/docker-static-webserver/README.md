# Simple Web Server using Docker

## Run the project

1. Build the Docker image: `docker build -t webserver-image .`
2. Run the Docker container: `docker run -dit --name static-webserver -p 8080:80 webserver-image`
3. Access the website: `http://localhost:8080`

## Docker Hub

This image is not pushed to Docker Hub, as it's a local project for demonstration purposes.

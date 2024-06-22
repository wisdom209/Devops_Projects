# Python Flask App using Docker

## Description

A simple web application built using Python, Flask, and Docker.

## Run the project

1. Build the Docker image: `docker build -t demo-flask-app .`
2. Run the Docker container: `docker run -dit -p 8080:5000 demo-flask-app`
3. Access the app: `http://localhost:8080`

## Docker Hub

This image is not pushed to Docker Hub, as it's a local project for demonstration purposes.

## Project Structure

* `app.py`: The Flask application entry point
* `Dockerfile`: The Dockerfile for building the image
* `requirements.txt`: The pip requirements file
* `README.md`: This file!

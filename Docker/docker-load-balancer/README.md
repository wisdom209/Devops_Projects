# Load Balancer using Docker and Nginx

## Overview

This project sets up a load balancer using Docker, a node-express app and Nginx, with multiple container instances. The load balancer distributes traffic across the containers using a round-robin algorithm.

## Prerequisites
   -  Docker installed on your system
   -  A basic understanding of Docker and Nginx

## Usage
	 - run the command `sudo docke-compose up -d --build"

## Testing
	 - Access http://localhost:3000 in your web browser to test the load balancer.
Configuration
	 - It prints a different host name for each time you access the given link

## Docker Images Used
    - node:latest (for the web application)
    - nginx:latest (for the load balancer)

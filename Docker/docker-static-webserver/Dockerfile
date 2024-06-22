# Set the base image
FROM nginx:latest

# Copy index.html into the container
COPY index.html /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Run nginx when container starts, specify setting to run container on foreground
CMD ["nginx", "-g", "daemon off;"]

#!/bin/bash
# Docker build script

echo "Building Docker image..."

# Build the image
docker build -t fastapi-microservice:latest .

echo "Docker image built successfully!"
echo "Run with: docker-compose up"

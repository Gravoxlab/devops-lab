# Docker Milestone 1 -First Containerized Web Service

## Context
First end-to-end Docker Deployment on AWS EC3 Ubuntu server.

## What was built 
- Installed Docker on EC3 
- Created Dockerfile using nginx base image 
- Ran container with port mapping (8080:80)
- Verified service using curl 

## Key Commands 
docker build -t my-first-web .
docker run -d -p 8080:80 my-first-web 
curl localhost:8080

## Outcome 
successfully deployed a working containerized web server.

## Key Learning 
A Docker image is a build artifact. A container is a running instance of that artifact.

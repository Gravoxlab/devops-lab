# Docker Installation and First Container Execution


## Objective 


Install Docker Engine on Ubuntu Linux and verify successful container execution. 

---

##Step 1 - Update System 

'''bash 
sudo apt update 

## Step 2 - Install Docker
sudo apt install docker.io -y 

## Step 3 - Start Docker Services 
sudo systemctl start Docker

## Step 4 - Enable Docker on Boot
sudo systemctl enable docker

## Step 5 - Verify Installation
docker --version
output: Docker Version 29. 1. 3

## Step 6 - Run First Container
docker run hello-world 

Result: 
Docker successfully pulled the hello-world image and executed a container.




OUTCOME

Docker Engine installed successfully and verified using a test container 



SKILLS DEMONSTRATED 
. Linux Package Management 
. Docker Installation 
. System Services Management
. Container Execution
. Image pulling from Docker Hub


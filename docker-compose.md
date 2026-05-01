
🧾 DevOps Execution Audit Trail (EC2 + Docker + Compose)
0. EC2 Access & System Prep
ssh -i key.pem ubuntu@<ec2-public-ip>
sudo apt update && sudo apt upgrade -y
1. Git Setup & Repo Initialization
git --version
git config --global user.name "your-name"
git config --global user.email "your-email"
git clone <repo-url>
cd <repo>
git checkout -b feature/devops-lab
2. Docker Installation & Validation
sudo apt install -y docker.io
sudo systemctl start docker
sudo systemctl enable docker
docker --version
sudo usermod -aG docker ubuntu
newgrp docker
docker run hello-world
3. Web App Container (Nginx)
Project structure
mkdir nginx-web && cd nginx-web
Dockerfile
FROM nginx:latest
COPY ./html /usr/share/nginx/html
EXPOSE 80
Build image
docker build -t custom-nginx .
Run container
docker run -d -p 8080:80 custom-nginx
4. Port Mapping Verification
curl http://localhost:8080
or externally:
http://<ec2-public-ip>:8080
5. Docker Compose Setup
Create compose file
nano docker-compose.yml
Example compose definition
version: "3"

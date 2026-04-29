# Devops Engineering Lab - Gravox Lab

## System Overview 

This  repository represents a structured DevOps engineering lab environment built on AWS EC2 Ubuntu infrastructure. 
The objective is to progressively simulate real-world cloud native system operations using Linux, Git, Docker, and CI/CD tooling 

## Infrastructure Context 

- Cloud provider: AWS EC2 
- Operating system: Ubuntu Server (22.04 LTS) 
- Access Layer: SSH-based terminal operations 
- Execution Environment: Linux CLI-based development 

## Core Toolchain 

- Git (Version control and source synchronization)
- Docker (containerization and runtime isolation) 
- Bash (automation and system scripting) 
- curl (service validation and HTTP probing) 

## Repository Architeture 


## Current Milestone status 

### Milestone 1: Containerized Baseline 

Completed: 
- Docker installation on EC2 
- Custom Docker image creation (nginx-based web server) 
- Container runtime execution with port mapping 
- service validation via HTTP request 

## Execution Flow Model
1. Code artifact creation (Dockerfile, scripts)
2. Image build process (Docker build)
3. Container instatation (Docker run)
4. Runtime Verification (curl, browser/logs) 

## Engineering Principle 

This repository follows an incremental infrastructure maturity model:

- Local System Scripting to containerization to ochestration (future)
- Manual execution to automated pipelines (future CI/CD integration)

## Next Phase 
- Docker networking and multi-container systems 
- Introduction to service isolation and inter-container communication 
- CI/CD pipeline integration using GitHub Actions

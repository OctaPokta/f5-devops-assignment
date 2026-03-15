# DevOps Intern Home Assignment

This repository contains the solution for the F5 DevOps Intern Home Assignment. It implements a containerized Nginx server and a separate test runner, automated using Docker Compose and GitHub Actions.

## Project Structure

* **nginx.conf**: Configures Nginx to listen on two ports (8080 for success, 8081 for error).
* **Dockerfile.nginx**: Builds the Ubuntu-based Nginx image.
* **test_script.py**: A Python script that validates the Nginx endpoints.
* **Dockerfile.test**: Builds the Python environment for the test script.
* **docker-compose.yml**: Orchestrates the build and execution of both services.
* **.github/workflows/ci.yml**: CI pipeline that builds, tests, and publishes artifacts.
 
## Design Decisions & Trade-offs

### 1. Choice of Base Images
* **Nginx:** Used `ubuntu:latest` as strictly required by the assignment constraints, rather than the lighter `nginx:alpine` image. This increases image size but ensures compliance with the requirements.
* **Tester:** Used `python:3.9-slim` for the test runner. Python was chosen for its readability and the robust `requests` library, making the test logic easy to understand and maintain.

### 2. Orchestration
* **Docker Compose:** Used a single `docker-compose.yml` to handle building and running both containers simultaneously. The flag `--abort-on-container-exit` ensures that the environment shuts down automatically once the tests finish, which is essential for CI automation.

### 3. CI/CD Pipeline
* The GitHub Actions workflow leverages the same Docker Compose command used locally.
* **Artifacts:** The pipeline uploads a `succeeded.txt` or `fail.txt` file depending on the test outcome, allowing for easy verification of build status without digging into logs.


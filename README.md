"""🚀 My First Dockerized Web App 🚀"""

Welcome to my first-ever project on GitHub! This is a simple but powerful "Hello, World!" web application built with Python and Flask, and containerized using Docker.

✨ About The Project
This project was created to learn the fundamentals of web development and DevOps. It demonstrates how to:

Create a basic web server using Flask.

Write a Dockerfile to define a container environment.

Build a Docker image and run it as a container.

🛠️ How To Run This Project
To get this project running on your own machine, you'll need to have Docker installed.

Clone the repository from GitHub:

git clone <your-github-repo-url>

Navigate into the project directory:

cd <your-project-directory>

Build the Docker image:
(This command tells Docker to build an image based on the Dockerfile)

docker build -t my-first-flask-app .

Run the Docker container:
(This command starts the container and maps port 8000 on your machine to port 8000 inside the container)

docker run -p 8000:8000 my-first-flask-app

See the result!
Open your web browser and go to http://localhost:8000. You should see the "Hello, World!" message.

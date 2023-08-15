Flask API containerized with Docker

## Getting started
To get started with `flask-docker` for local development, follow the instructions below. This requires you to have Docker/Docker Compose installed in addition to `make` to use the commands.
* `make network` to create the Docker network
* `make image` to build the Docker image
* `docker-compose up` to start the development server
* Navigate to [http://localhost:8000/randomize](http://localhost:8000/randomize) to explore the API

## Development commands
This project has a few useful development commands to ensure code quality and facilitate developer operations.
* `make network` to create the Docker network
* `make image` to build the Docker image
* `make shell` to access the bash shell inside the Docker container
* `make fmt` to run the code formatter (black)
* `make lint` to run the linter (ruff)
* `make test` to run the unit tests (pytest)

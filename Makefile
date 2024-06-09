SHELL := /bin/bash
export PYTHONPATH := .

DOCKER_IMAGE_NAME=restaurant-api
DOCKER_TAG=latest
PYTHON_VERSION=3.12

serve:
	@echo "Running the FastAPI APIs"
	cd src && poetry run uvicorn backend.main:app --host 0.0.0.0 --reload && cd ..


test:
	@echo "Running tests"
	poetry run python -m pytest --cov=src/backend --cov-report=term-missing


update-lockfile:
	@echo "Updating poetry.lock file..."
	poetry lock --no-update


docker-build:
	@echo "Building Docker image..."
	docker build -t $(DOCKER_IMAGE_NAME):$(DOCKER_TAG) .


build: update-lockfile docker-build
	@echo "Poetry lock file updated and Docker image built successfully."


# Target to run the Docker container
run:
	@echo "Running Docker container..."
	docker run -d -p 8000:8000 --name $(DOCKER_IMAGE_NAME) $(DOCKER_IMAGE_NAME):$(DOCKER_TAG)


# Clean target to remove the Docker container
docker-clean:
	@echo "Stopping and removing Docker container..."
	docker stop $(DOCKER_IMAGE_NAME) || true
	docker rm $(DOCKER_IMAGE_NAME) || true
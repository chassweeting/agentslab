# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Install debug tools
RUN apt-get update && apt-get install -y curl procps && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the Poetry configuration and lock files to the container
COPY poetry.lock pyproject.toml /app/

# Install Poetry
RUN pip install --no-cache-dir poetry

# Install dependencies defined in pyproject.toml
RUN poetry install --no-root --only main

# Copy the rest of the application code to the container
COPY src /app/src

# Set the environment variable for FastAPI
ENV MODULE_NAME="src.backend.main"

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the FastAPI application using Uvicorn
CMD ["poetry", "run", "uvicorn", "src.backend.main:app", "--host", "0.0.0.0", "--port", "8000"]

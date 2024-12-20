# Use the official Python image as a base
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    libpoppler-cpp-dev \
    poppler-utils \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install --upgrade pip && \
    pip install poetry

# Copy the project files
COPY . .

# Install project dependencies
RUN poetry install

# Set the entrypoint
CMD ["poetry", "run", "python", "src/main.py"]

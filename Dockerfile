# Dockerfile

# Use the official Python image as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python script into the container at /app
COPY cpu_intensive.py .

# Run the Python script when the container launches
CMD ["python", "cpu_intensive.py"]


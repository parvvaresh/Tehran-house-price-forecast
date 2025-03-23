# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables to ensure output is logged and prevent .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory in the container
WORKDIR /app

# Copy the requirements file first to leverage Docker cache
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

# Expose the port the app runs on
EXPOSE 5002

# Define environment variable for Flask if needed
ENV FLASK_APP=app.py

# Run the application
CMD ["python", "app.py"]

# Use the official Python base image
FROM python:3.9-slim

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# Install system dependencies
RUN apt-get update && apt-get install -y libmariadb-dev

# Set the working directory in the container
WORKDIR /app

# Copy the application files to the container
COPY requirements.txt .
COPY app.py .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that Flask listens on
EXPOSE 5000

# Run the Flask application
CMD ["flask", "run"]

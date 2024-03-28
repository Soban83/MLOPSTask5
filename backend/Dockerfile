# Use official Python image as base
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy and install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire backend directory
COPY . .

# Expose port
EXPOSE 5000

# Start Flask server
CMD ["python", "app.py"]

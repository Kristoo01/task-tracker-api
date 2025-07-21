# Use official lightweight Python image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy project files into the container
COPY . .

# Install Python dependencies
RUN python -m pip install --no-cache-dir -r requirements.txt

# Expose Flask port (important for container communication)
EXPOSE 5000

# Run the Flask application
CMD ["python", "app.py"]
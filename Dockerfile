# Use Python base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Set environment variables if needed
ENV PYTHONPATH=/app
ENV OLLAMA_HOST=host.docker.internal

# Expose the port
EXPOSE 8501

# Run the application
CMD ["streamlit", "run", "main.py"]
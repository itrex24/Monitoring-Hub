# Use lightweight Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the exporter script
COPY mock_metrics.py .

# Expose port
EXPOSE 8000

# Run the exporter
CMD ["python", "mock_metrics.py"]

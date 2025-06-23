# Use Python 3.12.1 for smaller image size
FROM python:3.12.1

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies (if needed)
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (for better Docker layer caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code (secrets excluded by .dockerignore)
COPY . .

# Create non-root user for security
RUN adduser --disabled-password --gecos '' appuser
RUN chown -R appuser:appuser /app
USER appuser

# Expose port
EXPOSE 8000

# Health check (optional)
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/docs || exit 1

# Command to run FastAPI with uvicorn
# Adjust the module:app part based on your file structure:
# If your FastAPI app is in main.py: uvicorn main:app
# If your FastAPI app is in app.py: uvicorn app:app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

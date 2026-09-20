FROM python:3.11-slim

WORKDIR /app

# Install system deps including psycopg2 requirements
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app
COPY . .

# Create instance directory
RUN mkdir -p instance

# Run as non-root
RUN useradd --create-home appuser
USER appuser

EXPOSE 5000

# Use $PORT if available, fallback to 5000
CMD gunicorn app:app --bind 0.0.0.0:${PORT:-5000} --workers 2 --timeout 120

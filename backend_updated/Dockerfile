FROM python:3.10-slim

# Create working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy only what’s needed first for caching
COPY requirements.txt /app/requirements.txt

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /app/requirements.txt flask-cors

# Copy full app
COPY . /app
COPY . .
# Expose Flask port
EXPOSE 5000

CMD ["python", "app.py"]
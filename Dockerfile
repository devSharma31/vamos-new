# Slim Python base
FROM python:3.11-slim

# System libs for Pillow (JPEG/PNG), psycopg2, etc. — common for Django
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libjpeg62-turbo-dev zlib1g-dev libpq-dev \
 && rm -rf /var/lib/apt/lists/*

# Workdir
WORKDIR /app

# Copy requirements pointers first for better layer caching
COPY requirements.txt requirements-ops.txt ./
COPY vamos/requirements.txt ./vamos/requirements.txt

# Install Python deps (ops file includes -r requirements.txt + gunicorn)
RUN pip install --upgrade pip && \
    pip install -r requirements-ops.txt

# Copy project source
COPY . .

# Environment (safe defaults for local/dev)
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=vamos.settings \
    PORT=8000

EXPOSE 8000

# Health-ish start: run Django via gunicorn
# If your module name is not 'vamos', change 'vamos.wsgi:application'
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "vamos.wsgi:application"]

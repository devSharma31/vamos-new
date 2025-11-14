FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PORT=8000

# Work at repo root first
WORKDIR /app

# System build tools (safe minimal)
RUN apt-get update && apt-get install -y --no-install-recommends build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install deps: keep thesis deps pure and add gunicorn via requirements-ops.txt
COPY requirements-ops.txt ./
COPY vamos/requirements.txt vamos/requirements.txt
RUN pip install -r requirements-ops.txt

# Copy source
COPY . .

# Switch to Django project root so `import vamos.wsgi` resolves
WORKDIR /app/vamos

# Optional: collectstatic if your project uses it (won't fail build if not configured)
# RUN python manage.py collectstatic --noinput || true

EXPOSE 8000

# Gunicorn entrypoint for nested layout: repo/vamos/vamos/wsgi.py
CMD ["gunicorn", "vamos.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "2", "--timeout", "60"]

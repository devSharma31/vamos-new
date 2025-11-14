FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PORT=8000

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements-ops.txt ./
COPY vamos/requirements.txt vamos/requirements.txt
RUN pip install -r requirements-ops.txt

COPY . .

# Put the parent of the inner "vamos/" package on PYTHONPATH
WORKDIR /app/vamos

EXPOSE 8000
CMD ["gunicorn", "vamos.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "2", "--timeout", "60"]

# Deployment Notes (per dissertation)

This mirrors the containerised deployment described in the MSc report:
- App container built from the repo’s `Dockerfile`
- Hosted on AWS (as per dissertation: Elastic Beanstalk w/ Docker OR equivalent)  
- Health endpoint and warmup/guardrail concepts are described in the report; this repo does not add new infra code.

## Local container run (repro)
# Build image
docker build -t vamos-app:latest .

# Run container (default port 8000)
docker run --rm -p 8000:8000 \
  -e DJANGO_SETTINGS_MODULE=vamos.settings \
  vamos-app:latest

# Open: http://localhost:8000/

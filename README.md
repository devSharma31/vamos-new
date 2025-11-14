# Cloud E-commerce Scalability — Autoscaling Guardrails (AWS ↔ Azure)

This repository mirrors the **MSc dissertation project** exactly (no new tools, numbers, or images beyond the report).

**Dissertation:** *Scalability and Performance Optimization in Cloud-based E-commerce & M-commerce Applications* — Devashish Sharma, Supervisor: Prof. Kashinath Basu, **submitted 02 Oct 2023**.  
PDF: [`/docs/Devashish_Sharma_MSc_2023.pdf`](docs/Devashish_Sharma_MSc_2023.pdf)

---

## TL;DR 
- Autoscaling stabilizes **p95 latency** and reduces **error rate** under bursty traffic.  
- **Guardrails** (min/max instances, warmup, health checks, cooldown) matter more than raw instance size.  
- A **documented rollback (~10 min)** keeps blast radius small.

> Platform in the report: AWS (Elastic Beanstalk, RDS, S3, CloudFront) with Azure mapping (App Service, Azure SQL, Blob, CDN).

---

## Architecture 
A simple web tier behind a load balancer with a managed DB and CDN.  
*(Diagram resides in the dissertation PDF; this repo uses text-only to avoid introducing new assets.)*

---

## DRA (Dynamic Resource Allocator) — Rules & Thresholds (from the report)
- **High traffic:** users > 1000 and (CPU > 70% **or** Memory > 80%) ⇒ scale up  
- **Low traffic:** users < 100 and CPU < 30% and Memory < 40% ⇒ scale down  
- **Normal:** 100–1000 users; hold or small adjustments within CPU/Mem 30–70%

*(Values quoted exactly as defined in the dissertation.)*

---

## Methodology 
- **Scenarios:** Baseline (no autoscale), Autoscale OFF, Autoscale ON (with warmup + `/health`).  
- **Metrics discussed:** p50/p95 latency, Error %, RPS, CPU.  
- **Artifacts:** Findings summarized here; the PDF is the source of record.

See: [`results/summary.md`](results/summary.md)

---

## Run the prototype
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
python manage.py runserver 
```

---
## Containerization
The prototype was containerised with Docker and hosted on AWS (as detailed in the thesis).  
This repository provides a reproducible `Dockerfile` for local runs.  

For a quick test:

**Local**
```bash
docker compose up --build
# http://127.0.0.1:8000
```
---
##AWS Elastic Beanstalk (Docker, AL2)

- Create an EB environment with Platform: Docker running on 64bit Amazon Linux 2.
- Zip and upload the repo root (must include Dockerfile).
- EB builds the image and runs Gunicorn with vamos.wsgi:application on port 8000.


## Scope & Integrity

This repo is an evidence mirror of the thesis.
- No new experiments or fabricated charts.
- No added tools not used in the report.
- CI/CD and Terraform live in separate repos to avoid overlap with this academic artifact.

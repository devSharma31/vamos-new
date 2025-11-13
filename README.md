# Cloud E-commerce Scalability — Autoscaling Guardrails (AWS ↔ Azure)

This repository mirrors the **MSc dissertation project** exactly (no new tools, numbers, or images beyond the report).

**Dissertation:** *Scalability and Performance Optimization in Cloud-based E-commerce & M-commerce Applications* — Devashish Sharma, Supervisor: Prof. Kashinath Basu, **submitted 02 Oct 2023**.  
PDF: [`/dissertation/Devashish_Sharma_MSc_2023.pdf`](dissertation/Devashish_Sharma_MSc_2023.pdf)

---

## TL;DR (as stated in the dissertation)
- Autoscaling stabilizes **p95 latency** and reduces **error rate** under bursty traffic.  
- **Guardrails** (min/max instances, warmup, health checks, cooldown) matter more than raw instance size.  
- A **documented rollback (~10 min)** keeps blast radius small.

> Platform in the report: AWS (Elastic Beanstalk, RDS, S3, CloudFront) with Azure mapping (App Service, Azure SQL, Blob, CDN).

---

## Architecture (per dissertation)
A simple web tier behind a load balancer with a managed DB and CDN.  
*(Diagram resides in the dissertation PDF; this repo uses text-only to avoid introducing new assets.)*

---

## DRA (Dynamic Resource Allocator) — Rules & Thresholds (from the report)
- **High traffic:** users > 1000 and (CPU > 70% **or** Memory > 80%) ⇒ scale up  
- **Low traffic:** users < 100 and CPU < 30% and Memory < 40% ⇒ scale down  
- **Normal:** 100–1000 users; hold or small adjustments within CPU/Mem 30–70%

*(Values quoted exactly as defined in the dissertation.)*

---

## Methodology (per dissertation)
- **Scenarios:** Baseline (no autoscale), Autoscale OFF, Autoscale ON (with warmup + `/health`).  
- **Metrics discussed:** p50/p95 latency, Error %, RPS, CPU.  
- **Artifacts:** Findings summarized here; the PDF is the source of record.

See: [`results/summary.md`](results/summary.md)

---

## Run the prototype (only if this was part of the thesis)
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
python manage.py runserver  # or the exact entrypoint you used in the report

# vamos-new# Cloud E-commerce Scalability — Autoscaling Guardrails (AWS ↔ Azure)

This repository mirrors the **MSc dissertation project** exactly (no added tools or claims).

**Title (as in report):** *Scalability and Performance Optimization in Cloud-based E-commerce & M-commerce Applications*  
**Author:** Devashish Sharma • **Supervisor:** Prof. Kashinath Basu • **Submission:** 02 Oct 2023  
**PDF:** [`/dissertation/Devashish_Sharma_MSc_2023.pdf`](dissertation/Devashish_Sharma_MSc_2023.pdf)

---

## TL;DR (from the dissertation)
- Autoscaling stabilizes **p95 latency** and reduces **error rate** under bursty traffic.  
- **Guardrails** (min/max instances, warmup, health checks, cooldown) matter more than raw instance size.  
- A **documented rollback (~10 min)** limits blast radius and makes change safe.

> This repo includes only what the dissertation used: code prototype, load-test artifacts, graphs, and the exact methodology/results.

---

## Architecture (per dissertation)
![Architecture](/docs/architecture.png)

**AWS stack:** Elastic Beanstalk (web), RDS (DB), S3 (assets), CloudFront (CDN)  
**Azure mapping:** App Service, Azure SQL, Blob Storage, Azure CDN

---

## Methodology (per dissertation)
- **Load tool(s):** JMeter (and *only* JMeter if that’s what the report used).  
- **Scenarios:** Baseline (no autoscale), Autoscale **OFF**, Autoscale **ON** (with warmup + `/health`).  
- **Metrics:** p50/p95 latency, Error %, RPS, CPU.

Artifacts:
- JMeter test plan: `tools/jmeter/plan.jmx`  
- Exported graphs: `/evidence/graphs/*.png`

---

## Results (from dissertation)
- ![Baseline](/evidence/graphs/baseline.png)
- ![Autoscale OFF](/evidence/graphs/autoscale-off.png)
- ![Autoscale ON](/evidence/graphs/autoscale-on.png)

See `/results/summary.md` for the table and commentary (fill with the exact numbers from the thesis).

---

## Guardrails (as implemented/evaluated)
- Min/Max instances (e.g., 2–6), warmup ~90s, health check = `/health`  
- CPU target ~60%, cooldown ~120s  
- Graceful shutdown; prepare blue/green before cutover

## Rollback (~10 minutes)
1. Swap to previous stable (Beanstalk blue/green OR App Service slot swap)  
2. Verify `/health` + smoke test checkout  
3. Watch errors/latency 5–10 min; keep or roll forward with config tweak  
4. Log **what changed/when/why**

---

## Run locally (prototype)
> Only if this was part of the dissertation. If the app is Django:

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
python manage.py runserver  # or the actual entrypoint you used

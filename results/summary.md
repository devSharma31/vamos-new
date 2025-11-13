# Results Summary (from dissertation)

**Scenarios evaluated (as in the report):**
- Baseline (no autoscale)
- Autoscale OFF
- Autoscale ON (with warmup + health checks)

**Reported outcomes:**
- Tail latency (p95) stabilized during spikes when **autoscale ON** compared to Baseline/Autoscale OFF.
- Error rate decreased under bursty load with **autoscale ON**.
- Guardrails (min/max instances, warmup, health check, cooldown) were more impactful than raw instance size.
- A documented rollback (~10 minutes) limited blast radius during bad deploys.

> Note: The dissertation did not provide separate downloadable numeric datasets or image assets; this repo intentionally mirrors the **textual findings** only and links to the PDF as the source of truth.

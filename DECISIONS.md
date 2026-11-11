# DECISIONS — ScamLens

This log records real product and engineering decisions. Add dated entries as implementation proceeds, including agent mistakes and how they were detected.

## 2026-11-11 — Keep the first version small
**Decision:** Build the first version with Python and Streamlit. Focus on text analysis, static URL inspection, an explainable report and evaluation.  
**Reason:** The course requires a runnable MVP at the Nov 16 checkpoint and a code freeze on Dec 6.  
**Trade-off:** Less custom UI control than a separate frontend/backend stack.

## 2026-11-11 — Inspect URL strings without visiting websites
**Decision:** Parse URL structure locally; do not fetch suspicious websites.  
**Reason:** Avoid contacting potentially malicious domains and keep the MVP safe and predictable.  
**Trade-off:** Cannot verify live page content or definitively establish site safety.

## 2026-11-11 — Evaluate against labeled cases
**Decision:** Use at least 40 manually labeled cases, classification metrics and a rule-based baseline.  
**Reason:** The course explicitly requires measurement of the AI feature.  
**Trade-off:** A small dataset is useful for comparison but not a complete real-world benchmark.

## Agent error / debugging records
*No agent coding sessions have been performed or recorded in this starter repository yet. Add genuine findings here once they occur.*

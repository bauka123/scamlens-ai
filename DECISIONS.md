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

## 2026-11-24 — Implement deterministic-first MVP
**Decision:** Keep rule and URL analysis separate from optional API analysis, then combine all evidence in a coordinator.  
**Reason:** This preserves an explainable offline fallback and prevents API failure from removing core functionality.  
**Trade-off:** The deterministic baseline may miss unusual phrasing and cannot assess live reputation or page content.

## 2026-11-24 — Use an OpenAI-compatible HTTP interface
**Decision:** Implement optional API calls through environment-configured endpoint, key and model variables.  
**Reason:** It supports provider flexibility without adding an SDK dependency.  
**Trade-off:** API responses are parsed defensively and may fail under provider-specific formats.

## 2026-11-24 — URL extraction missed IP literals
**Observed issue:** The initial URL regex did not extract `http://192.168.1.20/login`, so the static inspector could not score an otherwise obvious warning URL.  
**Detection:** A pytest assertion for the coordinator remained `Medium` instead of `High`.  
**Fix:** Extended the URL regex to recognize IPv4 and bracketed IPv6 literals.  
**Result:** The focused test suite passed 10/10 after the fix.

## 2026-11-24 — Python environment mismatch
**Observed issue:** The first test command used Python 3.11, but `pytest` was not installed in that environment.  
**Detection:** `python -m pytest` returned `No module named pytest`.  
**Fix:** Used the existing Python 3.11 Conda environment and installed the declared dependencies.  
**Important:** No external API key was used or exposed during testing.

## 2026-11-24 — Baseline evaluation result
**Observed result:** A fixed 40-case manually labeled set produced accuracy `0.85`, precision `1.00`, recall `0.6667`, and F1 `0.80`.  
**Interpretation:** This is a fixed-sample result, not a real-world guarantee.

## Agent error / debugging records
See the dated entries above. Genuine development commands and observed results are also summarized in `agent-logs/`.

# ScamLens — AI-Powered Scam Detection Assistant

**Course:** CSS4007 Final Project (Narxoz University)  
**Status:** First working MVP

## About
ScamLens helps people examine potentially fraudulent messages and suspicious links. It combines transparent deterministic checks with optional API-based text analysis. The result is a Low, Medium, or High risk level with evidence and safe actions.

**ScamLens is decision support, not a guarantee that a message or URL is legitimate or fraudulent.**

## MVP features
- Streamlit message input and analysis button
- Rule checks for urgency, credential requests, rewards, impersonation, fees, remote access and contact moves
- Static URL parsing for IP addresses, unusual hosts, long URLs, non-standard ports and other warning signals
- Evidence and independently actionable safety recommendations
- Optional AI analysis using an OpenAI-compatible API
- Explicit fallback status when no key is configured or the API fails
- No storage of user messages by default

## Safety
- ScamLens never opens, crawls, fetches or previews suspicious URLs.
- URL checks only inspect strings locally.
- API analysis is disabled unless the user enables it.
- API use sends the pasted message to the configured endpoint; never paste passwords or private data.
- Keep real keys in environment variables and never commit `.env`.

## Setup
Requires Python 3.11+.

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cp .env.example .env
streamlit run app.py
```

Optional API variables:

```bash
SCAMLENS_API_KEY=your_key
SCAMLENS_API_URL=https://api.openai.com/v1/chat/completions
SCAMLENS_MODEL=gpt-4o-mini
```

`OPENAI_API_KEY` is also accepted. `.env` loading is not performed automatically; export variables in the shell or configure them in the deployment environment.

## Tests and evaluation
```bash
python -m pytest -q
python evaluation.py
```

The unit suite verifies rules, URL inspection, coordination, empty input and API fallback behavior. `evaluation.py` evaluates 40 manually labeled cases with accuracy, precision, recall and F1.

A run on 2026-11-24 with Python 3.11.16 recorded: 40 cases, accuracy 0.85, precision 1.00, recall 0.6667 and F1 0.80. This fixed set is not proof of real-world performance.

## Known limitations
- Static URL checks cannot prove whether a domain is malicious or safe.
- Keyword rules can miss novel wording and can false-positive ordinary urgency.
- Optional AI responses can be unavailable or imperfect and are treated defensively.
- No live reputation, registration, certificate or page-content checks are included.

## Repository documents
- [`PLAN.md`](PLAN.md) — scope and milestones
- [`AGENTS.md`](AGENTS.md) — coding and safety instructions
- [`DECISIONS.md`](DECISIONS.md) — product and engineering decisions
- [`agent-logs/`](agent-logs) — authentic agent-session records

## Team
To be completed by the registered team members. Every member is responsible for code they commit and should be able to explain their contribution.

# ScamLens — AI-Powered Scam Detection Assistant

**Course:** CSS4007 Final Project (Narxoz University)  
**Status:** Planning and initial repository setup

## About the project
ScamLens is a Python/Streamlit application that helps people examine potentially fraudulent messages and suspicious links. It combines an AI-based message analysis with a *non-invasive* URL structure check to produce an explainable risk assessment and practical safety suggestions.

**Important:** ScamLens is a decision-support tool, not a guarantee that a message or URL is legitimate or fraudulent.

## Planned MVP
1. Analyze pasted text for social-engineering indicators (urgency, impersonation, requests for credentials, etc.).
2. Inspect URL structure without opening or crawling suspicious websites.
3. Combine results into a Low / Medium / High assessment, with evidence and recommended safe actions.
4. Evaluate classifications on 40 hand-labeled examples and compare with a rule-based baseline.

## Planned stack
- Python 3.11+
- Streamlit
- An LLM API (provider and free-tier access to be verified)
- Python standard library for URL parsing
- GitHub Copilot Agent Mode for agentic development

## Repository documents
- [`PLAN.md`](PLAN.md): planned scope and checkpoints, drafted before coding.
- [`AGENTS.md`](AGENTS.md): instructions for the coding agent.
- [`DECISIONS.md`](DECISIONS.md): major trade-offs and debugging decisions.
- [`agent-logs/`](agent-logs/): real exported coding-agent sessions to be added during development.
- [`tests/`](tests/): evaluation and software tests, to be implemented.
- `REFLECTION.md`: to be written after hands-on work with the agent.

## Getting started
This repository currently contains **planning documents only**. It is **not yet a runnable application**. Implementation and installation steps will be added during development, with instructions tested on a clean machine before the December 6 code freeze.

## Safety and privacy
- Never commit API keys, credentials, or private user messages.
- Do not visit potentially malicious URLs during analysis.
- Use dummy examples and appropriately licensed public data for tests.
- Show uncertainty and actionable recommendations rather than definitive assurances.

## Team
To be completed by the registered team members. Every member is responsible for their own code, commits, and contribution at the defense.

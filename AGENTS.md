# Instructions for the Coding Agent — ScamLens

You are assisting a student team building the CSS4007 final project. The project must remain explainable, testable, safe and manageable within five weeks.

## Before editing
1. Read `PLAN.md`, `README.md`, and `DECISIONS.md`.
2. Summarize the requested change and identify the smallest end-to-end increment.
3. Explain any new dependency, external service, or API before introducing it.
4. Ask before expanding scope or adding paid services.

## During implementation
- Use Python 3.11+ and Streamlit for the first working version.
- Keep the AI call separate from deterministic URL checks.
- Never open, crawl, fetch, execute, or preview suspicious URLs; parse URL strings only.
- Do not promise that any classification is 100% correct.
- Provide evidence and uncertain/unknown outcomes where necessary.
- Keep secrets in environment variables; commit only `.env.example`.
- Prefer simple dependencies and small, reviewable commits.

## Testing and reporting
- Add tests for code you change and run them if the environment allows.
- Record commands actually executed and results actually observed. Never invent green tests or logs.
- Create an evaluation process against a manually labeled set and a rule-based baseline.
- Report known limitations and failure cases.

## Student ownership and academic integrity
- Explain the code and decisions so every team member can defend their contribution.
- Save 3–5 authentic important sessions in `agent-logs/` (transcript or export).
- Record significant decisions, agent mistakes and how the team noticed them in `DECISIONS.md`.
- Do not claim the agent ran a command or fixed a bug unless it actually did.

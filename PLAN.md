# PLAN — ScamLens

**Created before application code.**  
**Course:** CSS4007 Final Project

## 1. Problem and users
People receive potentially fraudulent messages through email, SMS, and messengers. They may struggle to identify impersonation, urgent pressure, or unsafe links. Target users are everyday internet users seeking a clear explanation before taking action.

## 2. Scope
### Must-have MVP
- Text input and a working analysis button in Streamlit.
- Tool A: message analysis through an LLM with a structured response.
- Tool B: static URL checks using parsing and deterministic warning indicators (no browsing).
- A coordinator combining tool outputs into an explainable risk category and safety advice.
- Error handling and safe default behavior when an API is unavailable.
- Evaluated results on at least 40 hand-labeled test cases, compared to a rule-based baseline.

### Stretch goals (only after MVP)
- Local history for a user's own analyses.
- Downloadable PDF report.

### Out of scope
- Website crawling or visiting potentially malicious links.
- Collection of private personal data.
- Payment handling, automated reporting or website takedown.
- Claims of guaranteed scam detection.

## 3. Proposed architecture
Streamlit UI -> analysis coordinator -> [LLM text analyzer, static URL inspector] -> evidence and risk report. Store no user input by default.

## 4. Evaluation plan
- Build a **manually labeled** evaluation set with at least 40 examples across scam-like and ordinary messages.
- Include multiple fraud styles: urgency, fake support, prize scam, credential requests, suspicious URL, and benign messages.
- Keep labels independent of model output and document labeling criteria.
- Measure accuracy, precision, recall, and F1 for binary scam/not-scam; separately check clarity of explanations with a simple human rubric.
- Compare against a transparent keyword/rule-based baseline. Preserve both successes and failures.
- Note that a small fixed test set does not prove performance in the wild.

## 5. Milestones
- **Nov 11:** Submit one-page proposal in Canvas.
- **By Nov 16:** Deliver first end-to-end runnable version; commit URL, PLAN.md, AGENTS.md, and initial real agent logs.
- **By Dec 6:** Freeze at tag `v1.0`; test fresh setup, document evaluation, complete reflection, keep repository free of secrets.
- **Dec 7–19:** 5-minute demo, 2–3-minute backup video, agent-process discussion, team Q&A.

## 6. Team roles (assign actual names after team is registered)
- Member 1: User interface, integration, README, demo.
- Member 2: Agent orchestration, LLM integration, URL inspection.
- Member 3 if present: Evaluation dataset, testing, QA, backup video.
Every member must make traceable Git commits and explain their own work.

## 7. Engineering and safety checks
- No live visits to untrusted URLs, no fetching their content.
- Model response parsing and defensive failure modes.
- Unit tests for URL parsing and baseline rules.
- Do not expose secrets in code, commits, screenshots, logs or sample data.
- Actual agent development must be performed in an IDE/terminal tool, with 3–5 authentic session records.

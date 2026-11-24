"""Optional OpenAI-compatible API analysis with defensive fallback behavior."""

from __future__ import annotations

import json
import os
from urllib import request
from urllib.error import HTTPError, URLError


def analyze_with_llm(message: str) -> dict:
    api_key = os.getenv("SCAMLENS_API_KEY") or os.getenv("OPENAI_API_KEY")
    if not api_key:
        return {"status": "fallback", "reason": "No API key configured", "risk": None, "evidence": []}

    endpoint = os.getenv("SCAMLENS_API_URL", "https://api.openai.com/v1/chat/completions")
    model = os.getenv("SCAMLENS_MODEL", "gpt-4o-mini")
    prompt = (
        "Analyze the following message for scam indicators. Return only valid JSON with keys "
        "risk ('low', 'medium', or 'high'), evidence (array of short strings), and uncertainty "
        "(short string). Do not claim certainty. Message: " + message
    )
    payload = json.dumps({"model": model, "temperature": 0,
                          "messages": [{"role": "system", "content": "You are a cautious scam-analysis assistant. Never claim 100% certainty."},
                                       {"role": "user", "content": prompt}]}).encode()

    req = request.Request(endpoint, data=payload, headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}, method="POST")
    try:
        with request.urlopen(req, timeout=15) as response:
            body = json.loads(response.read().decode("utf-8"))
    except (HTTPError, URLError, TimeoutError) as exc:
        return {"status": "fallback", "reason": f"API unavailable: {exc}", "risk": None, "evidence": []}

    try:
        content = body["choices"][0]["message"]["content"]
        result = json.loads(content)
    except (KeyError, IndexError, json.JSONDecodeError, TypeError):
        return {"status": "fallback", "reason": "API returned a malformed response", "risk": None, "evidence": []}

    risk = str(result.get("risk", "low")).lower()
    if risk not in {"low", "medium", "high"}:
        risk = "low"
    evidence = result.get("evidence", [])
    if not isinstance(evidence, list):
        evidence = []
    uncertainty = str(result.get("uncertainty", "The result is uncertain."))
    return {"status": "available", "risk": risk, "evidence": evidence, "uncertainty": uncertainty}

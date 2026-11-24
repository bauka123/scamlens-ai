"""Combine transparent rules and optional AI analysis into a final report."""

from __future__ import annotations

from .rules import analyze_message
from .url_inspector import inspect_urls


def risk_level(rule_score: int, ai_risk: str | None = None) -> str:
    effective = rule_score
    if ai_risk == "high":
        effective += 3
    elif ai_risk == "medium":
        effective += 1

    if effective >= 7:
        return "High"
    if effective >= 3:
        return "Medium"
    return "Low"


def analyze(message: str, ai_result: dict | None = None) -> dict:
    message = message.strip()
    if not message:
        return {"risk": "Unknown", "rule_score": 0, "evidence": ["No message was provided"], "urls": [], "recommendations": ["Paste a message before analysis."]}

    rules = analyze_message(message)
    urls = inspect_urls(message)
    url_score = sum(url_result["score"] for url_result in urls)
    rule_score = rules["score"] + url_score

    evidence = list(rules["evidence"])
    for url_result in urls:
        if url_result["evidence"]:
            evidence.append(f"URL {url_result['url']}: " + "; ".join(url_result["evidence"]))
        else:
            evidence.append(f"URL {url_result['url']}: no suspicious static structure signals found")

    ai_risk = ai_result.get("risk") if ai_result else None
    level = risk_level(rule_score, ai_risk)

    if ai_result:
        ai_evidence = ai_result.get("evidence", [])
        if isinstance(ai_evidence, list):
            evidence.extend(f"AI: {item}" for item in ai_evidence if isinstance(item, str))

    recommendations = []
    if level == "High":
        recommendations.append("Do not reply, pay, share credentials or install anything.")
        recommendations.append("Verify the organization using a phone number or website you independently know.")
    elif level == "Medium":
        recommendations.append("Treat the message cautiously and verify the request through an independent channel.")
        recommendations.append("Do not use any link or QR code in the message to enter sensitive information.")
    else:
        recommendations.append("No strong warning signals were found, but this is not a guarantee of safety.")
        recommendations.append("Use normal caution and independently verify unexpected requests.")

    if urls:
        recommendations.append("URL results are structural only: ScamLens did not visit or scan these pages.")

    ai_status = ai_result.get("status", "not_requested") if ai_result else "not_requested"
    return {
        "risk": level,
        "rule_score": rule_score,
        "evidence": evidence or ["No strong rule-based warning signals found"],
        "urls": urls,
        "recommendations": recommendations,
        "ai_status": ai_status,
    }

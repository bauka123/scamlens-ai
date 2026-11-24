"""Transparent deterministic phishing indicators used by ScamLens."""

from __future__ import annotations

import re

INDICATORS = (
    ("Urgency or threat", r"\b(urgent|immediately|act now|today only|last chance|account.{0,20}(suspend|close)|within\s+(?:24|48)\s+hours)\b", 2),
    ("Credential or payment request", r"\b(password|otp|one-time (?:code|password)|pin|credit card|bank details|gift card|crypto|bitcoin|wallet seed|recovery phrase)\b", 3),
    ("Unrealistic reward", r"\b(prize|lottery|winner|inheritance|million dollars|free (?:money|gift|cash)|claim.{0,20}(reward|prize))\b", 2),
    ("Authority or impersonation", r"\b(bank|police|tax|customs|courier|support team|security team|delivery service|government)\b", 1),
    ("Delivery or fee request", r"\b(delivery fee|shipping fee|customs fee|processing fee|tracking (?:fee|payment)|reschedule delivery)\b", 2),
    ("Remote access request", r"\b(remote (?:access|desktop)|teamviewer|anydesk|screen sharing|install.{0,20}(app|software))\b", 2),
    ("Suspicious contact move", r"\b(whatsapp|telegram|signal|dm me|move.{0,15}(chat|private)|do not tell)\b", 1),
)


def analyze_message(message: str) -> dict:
    lowered = message.lower()
    evidence: list[str] = []
    score = 0

    for label, pattern, weight in INDICATORS:
        match = re.search(pattern, lowered, re.I)
        if match:
            excerpt = message[max(0, match.start() - 20):match.end() + 20].strip().replace("\n", " ")
            evidence.append(f"{label}: “{excerpt[:100]}”")
            score += weight

    return {"score": score, "evidence": evidence}

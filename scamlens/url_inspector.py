"""Static, non-network URL structure inspection for ScamLens."""

from __future__ import annotations

import ipaddress
import re
from urllib.parse import urlsplit

_URL_PATTERN = re.compile(
    r"(?:https?://(?:\d{1,3}(?:\.\d{1,3}){3}|\[[0-9A-Fa-f:]+\])(?:[:/?#][^\s]*)?|(?:https?://)?(?:[\w@.-]+\.[A-Za-z]{2,}|localhost)(?:[:/?#][^\s]*)?)",
    re.I,
)


def extract_urls(text: str) -> list[str]:
    """Extract plausible URL-like strings without opening or resolving them."""
    return list(dict.fromkeys(match.group(0).rstrip(".,;!?)\"'") for match in _URL_PATTERN.finditer(text)))


def inspect_url(raw_url: str) -> dict:
    """Inspect URL text; this function never performs DNS or HTTP requests."""
    value = raw_url.strip()
    parsed = urlsplit(value if "://" in value else f"//{value}")
    host = (parsed.hostname or "").lower().rstrip(".")
    evidence: list[str] = []
    score = 0

    if not host:
        return {"url": value, "host": "", "score": 1, "evidence": ["No recognizable host was found"], "unknown": True}

    if host.startswith("www."):
        host_label = host[4:].lower()
    else:
        host_label = host.lower()

    suspicious_tlds = ("xyz", "top", "click", "link", "work", "zip", "icu", "rest")
    if host_label.endswith(tuple(f".{tld}" for tld in suspicious_tlds)):
        evidence.append("Host uses a commonly abused or low-cost top-level domain")
        score += 2

    if "@" in value:
        evidence.append("URL contains '@', which can hide the true destination")
        score += 3

    try:
        ipaddress.ip_address(host)
        evidence.append("URL uses an IP address instead of a named domain")
        score += 2
    except ValueError:
        pass

    if "-" in host_label:
        evidence.append("Host contains hyphens, which are often used to imitate brands")
        score += 1

    if re.search(r"\d{5,}", host_label):
        evidence.append("Host contains an unusual long numeric sequence")
        score += 1

    if len(host_label) >= 30:
        evidence.append("Host name is unusually long")
        score += 1

    port = parsed.port if "://" in value else None
    if port is not None and port not in (80, 443):
        evidence.append("URL specifies a non-standard port")
        score += 2

    if len(value) > 100:
        evidence.append("URL is unusually long")
        score += 1

    return {"url": value, "host": host, "score": score, "evidence": evidence, "unknown": False}


def inspect_urls(text: str) -> list[dict]:
    return [inspect_url(url) for url in extract_urls(text)]

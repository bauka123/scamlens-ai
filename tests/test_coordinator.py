from scamlens.coordinator import analyze


def test_high_risk_message_combines_evidence_and_advice():
    report = analyze("Your bank account is suspended. Send your OTP and password immediately to http://192.168.1.20/login")
    assert report["risk"] == "High"
    assert any("bank" in item.lower() or "credential" in item.lower() for item in report["evidence"])
    assert report["urls"]
    assert any("did not visit" in item for item in report["recommendations"])


def test_empty_message_is_unknown():
    report = analyze("  ")
    assert report["risk"] == "Unknown"


def test_benign_message_is_low_risk():
    report = analyze("Hello, are we still meeting tomorrow at 10?")
    assert report["risk"] == "Low"

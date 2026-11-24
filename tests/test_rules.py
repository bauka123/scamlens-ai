from scamlens.rules import analyze_message


def test_detects_urgency_and_credentials():
    report = analyze_message("Act now! Send your OTP and password immediately.")
    assert report["score"] >= 5
    assert any("Urgency" in item for item in report["evidence"])
    assert any("Credential" in item for item in report["evidence"])


def test_benign_message_has_no_strong_evidence():
    report = analyze_message("Hello, are we still meeting tomorrow at 10?")
    assert report["score"] == 0
    assert report["evidence"] == []

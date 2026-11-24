from scamlens.url_inspector import extract_urls, inspect_url


def test_extracts_unique_urls():
    text = "Visit https://example.com/a and https://example.com/a"
    assert extract_urls(text) == ["https://example.com/a"]


def test_ip_address_is_flagged():
    report = inspect_url("http://192.168.1.20/login")
    assert report["score"] >= 2
    assert any("IP address" in item for item in report["evidence"])


def test_at_sign_is_flagged():
    report = inspect_url("https://trusted.example.com@evil.xyz/login")
    assert report["score"] >= 3
    assert any("@" in item for item in report["evidence"])


def test_normal_https_url_has_no_static_evidence():
    report = inspect_url("https://example.org/help")
    assert report["host"] == "example.org"

from scamlens.llm import analyze_with_llm


def test_missing_api_key_returns_fallback(monkeypatch):
    monkeypatch.delenv("SCAMLENS_API_KEY", raising=False)
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    result = analyze_with_llm("A test message")
    assert result["status"] == "fallback"
    assert result["risk"] is None
    assert "No API key" in result["reason"]

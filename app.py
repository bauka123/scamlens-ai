"""Streamlit interface for ScamLens."""

import streamlit as st

from scamlens.coordinator import analyze
from scamlens.llm import analyze_with_llm


st.set_page_config(page_title="ScamLens", page_icon="🛡️", layout="wide")

st.title("🛡️ ScamLens")
st.caption("Explainable scam-risk support — not a guarantee of legitimacy or fraud")

with st.expander("Privacy and safety", expanded=False):
    st.write("The pasted text is processed locally for rule checks and URL structure checks. ScamLens does not visit, crawl, or fetch suspicious links.")
    st.write("If API analysis is enabled, the message is sent to the configured API. Do not paste passwords or private personal data.")

message = st.text_area("Paste a message to analyze", height=180, placeholder="Paste an email or text message here…")
use_llm = st.checkbox("Use optional AI analysis", value=False)

if st.button("Analyze message", type="primary"):
    if not message.strip():
        st.warning("Enter a message first.")
    else:
        ai_result = analyze_with_llm(message) if use_llm else None
        report = analyze(message, ai_result)

        risk_colors = {"High": "red", "Medium": "orange", "Low": "green", "Unknown": "gray"}
        st.markdown(f"### Risk level: :{risk_colors[report['risk']]}[{report['risk']}]")
        st.progress(min(report["rule_score"] / 12, 1.0), text=f"Rule and URL score: {report['rule_score']}")

        if ai_result:
            if ai_result["status"] == "available":
                st.success("AI analysis available")
                st.write(f"AI uncertainty: {ai_result.get('uncertainty', 'Not provided')}")
            else:
                st.warning("Fallback result used — AI analysis is unavailable")
                st.write(ai_result["reason"])
        else:
            st.info("Deterministic fallback result — optional AI analysis was not requested")

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Evidence")
            for item in report["evidence"]:
                st.write("• " + item)
        with col2:
            st.subheader("Safety recommendations")
            for item in report["recommendations"]:
                st.write("• " + item)

        if report["urls"]:
            st.subheader("URL structure inspection")
            for url in report["urls"]:
                st.code(url["url"])
                st.write("Host:", url["host"] or "Not recognized")
                st.write("Static warning score:", url["score"])

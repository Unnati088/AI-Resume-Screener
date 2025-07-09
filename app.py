import streamlit as st
from resume_parser import extract_text_from_pdf
from scorer import score_resume

st.set_page_config(page_title="AI Resume Screener", layout="centered")

st.title("🧠 AI Resume Screener")
st.markdown("Upload resumes and a job description — get ranked results based on skill and keyword match.")

uploaded_files = st.file_uploader("📄 Upload Resume PDFs", type="pdf", accept_multiple_files=True)
job_description = st.text_area("📝 Paste Job Description")

if st.button("🔍 Score Resumes"):
    if uploaded_files and job_description.strip():
        results = []
        for file in uploaded_files:
            text = extract_text_from_pdf(file)
            score, matched = score_resume(text, job_description)
            results.append((file.name, score, matched))

        sorted_results = sorted(results, key=lambda x: x[1], reverse=True)

        st.markdown("### 🏆 Ranked Resumes")
        for i, (name, score, matched) in enumerate(sorted_results, 1):
            st.write(f"**{i}. {name}** — Score: `{score}%`")
            st.caption(f"🔑 Matched Keywords: {', '.join(matched)}")
    else:
        st.warning("Please upload at least one resume and enter a job description.")

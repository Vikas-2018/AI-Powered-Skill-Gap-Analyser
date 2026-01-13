import pandas as pd
import streamlit as st

from text_utils import extract_text
from skills import extract_skills
from matcher import find_skill_gap, calculate_match_percentage

st.title("AI-Powered Skill Gap Analyzer")

resume = st.file_uploader("Upload Resume", ["pdf", "docx", "txt"])
jd = st.file_uploader("Upload Job Description", ["pdf", "docx", "txt"])

if resume and jd:
    # Extract text
    resume_text = extract_text(resume)
    jd_text = extract_text(jd)

    # Extract skills
    resume_tech, resume_soft = extract_skills(resume_text)
    jd_tech, jd_soft = extract_skills(jd_text)

    # Skill gap analysis (technical skills)
    missing_skills = find_skill_gap(resume_tech, jd_tech)

    # Match percentage
    match_percent = calculate_match_percentage(
        resume_tech, jd_tech, missing_skills
    )

    # Display results
    st.subheader("Resume Technical Skills")
    st.write(resume_tech)

    st.subheader("Resume Soft Skills")
    st.write(resume_soft)

    st.subheader("Job Description Technical Skills")
    st.write(jd_tech)

    st.subheader("Missing Technical Skills")
    st.write(missing_skills)

    st.subheader("Skill Match Percentage")
    st.success(f"{match_percent}% match")

    # CSV Report
    report = pd.DataFrame({
        "Resume Technical Skills": pd.Series(resume_tech),
        "Job Description Technical Skills": pd.Series(jd_tech),
        "Missing Skills": pd.Series(missing_skills)
    })

    st.download_button(
        label="Download Skill Gap Report (CSV)",
        data=report.to_csv(index=False),
        file_name="skill_gap_report.csv",
        mime="text/csv"
    )


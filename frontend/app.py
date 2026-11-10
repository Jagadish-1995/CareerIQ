import streamlit as st

st.set_page_config(
    page_title="CareerIQ",
    page_icon="🎯",
    layout="wide"
)

st.title("CareerIQ")
st.subheader("AI Career Intelligence & Interview Platform")

st.write(
    "Understand your skills, match your career, and master your interview."
)

st.divider()

st.header("Get Started")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Resume")
    st.write("Upload your resume for AI-powered analysis.")

with col2:
    st.subheader("Job Description")
    st.write("Analyze how well your profile matches a target job.")

st.info("CareerIQ is under development.")
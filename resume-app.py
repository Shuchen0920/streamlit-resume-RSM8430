import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Eliana Song - Interactive Resume")

st.header("About Me")
st.write(
"Finance and data analyst with experience in portfolio analytics, "
"investment operations, and data automation using Python and SQL."
)

# WIDGET 1
experience = st.slider("Years of Experience in Data / Finance", 0, 10, 2)
st.write("Years of experience:", experience)

# WIDGET 2
career_interest = st.selectbox(
    "Select Area of Interest",
    ["Investment Analytics", "Data Science", "Risk Analytics", "Financial Modeling"]
)

st.write("Career interest:", career_interest)

# WIDGET 3
show_projects = st.checkbox("Show Project Experience")

if show_projects:
    st.write("Systemic Risk & Default Forecasting with Social Network Analysis")
    st.write("Built predictive model achieving >98% ROC-AUC")

# TABLE
st.header("Education")

education = pd.DataFrame({
    "Degree": [
        "Master of Management Analytics",
        "Bachelor of Business Administration (Business Analytics)"
    ],
    "School": [
        "University of Toronto - Rotman School of Management",
        "National University of Singapore"
    ],
    "Year": ["2025 - Present", "2020 - 2024"]
})

st.table(education)

# CHART
st.header("Technical Skills")

skills = pd.DataFrame({
    "Skill": ["Python", "SQL", "Tableau", "Financial Analysis"],
    "Level": [90, 85, 80, 75]
})

fig, ax = plt.subplots()
ax.bar(skills["Skill"], skills["Level"])
ax.set_ylabel("Skill Level")
ax.set_title("Skill Proficiency")

st.pyplot(fig)
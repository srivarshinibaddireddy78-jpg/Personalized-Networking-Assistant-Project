import streamlit as st
import requests
import json
from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# Backend URL
API_URL = "http://127.0.0.1:8000"

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Personalized Networking Assistant",
    page_icon="🤝",
    layout="wide"
)

# --------------------------------------------------
# Session State
# --------------------------------------------------

if "analysis" not in st.session_state:
    st.session_state.analysis = None

if "conversation" not in st.session_state:
    st.session_state.conversation = ""

if "fact_result" not in st.session_state:
    st.session_state.fact_result = ""

# --------------------------------------------------
# PDF Generator
# --------------------------------------------------

def create_pdf(analysis, conversation):

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph(
            "Personalized Networking Assistant Report",
            styles["Title"]
        )
    )

    story.append(Spacer(1,20))

    story.append(
        Paragraph(
            "<b>Event Analysis</b>",
            styles["Heading2"]
        )
    )

    if analysis:

        for key, value in analysis.items():

            story.append(
                Paragraph(
                    f"<b>{key}</b>: {value}",
                    styles["BodyText"]
                )
            )

    story.append(Spacer(1,20))

    story.append(
        Paragraph(
            "<b>Conversation Starter</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            conversation,
            styles["BodyText"]
        )
    )

    doc.build(story)

    buffer.seek(0)

    return buffer
# --------------------------------------------------
# Custom CSS
# --------------------------------------------------

st.markdown("""
<style>

.main {
    background-color: #f8fafc;
}

.block-container {
    padding-top: 2rem;
}

h1 {
    color: #1e3a8a;
}

h2, h3 {
    color: #1e40af;
}

.stButton > button {
    width: 100%;
    height: 50px;
    border-radius: 12px;
    border: none;
    background: linear-gradient(90deg,#2563eb,#7c3aed);
    color: white !important;
    font-size: 18px;
    font-weight: bold;
}

.stButton > button:hover {
    background: linear-gradient(90deg,#1d4ed8,#6d28d9);
}

.card {
    background-color: white;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.08);
    margin-bottom: 15px;
}

.footer {
    text-align:center;
    color:gray;
    margin-top:40px;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("🤝 Personalized Networking Assistant")

st.markdown(
"""
Generate personalized networking conversations using AI.

This application can:

✅ Analyze networking events

✅ Generate personalized conversation starters

✅ Fact-check networking topics

✅ Download your report as a PDF
"""
)

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

st.sidebar.title("📌 Menu")

st.sidebar.info("""
### Personalized Networking Assistant

This project helps you:

- Analyze events
- Generate AI conversations
- Verify information
- Download PDF reports

**Powered by FastAPI + Gemini + Streamlit**
""")

st.sidebar.success("Epic 4 - Frontend UI")
# --------------------------------------------------
# Event Analysis
# --------------------------------------------------

st.markdown("---")
st.header("📝 Event Analysis")

name = st.text_input(
    "Your Name",
    placeholder="Enter your name"
)

profession = st.text_input(
    "Profession",
    placeholder="Software Engineer, Student, etc."
)

interests = st.text_input(
    "Interests (comma separated)",
    placeholder="AI, Python, Machine Learning"
)

event_name = st.text_input(
    "Event Name",
    placeholder="AI Networking Summit 2026"
)

if st.button("🔍 Analyze Event"):

    payload = {
        "name": name,
        "profession": profession,
        "interests": [
            i.strip() for i in interests.split(",")
        ],
        "event_name": event_name
    }

    try:

        response = requests.post(
            f"{API_URL}/analyze-event",
            json=payload
        )

        if response.status_code == 200:

            st.session_state.analysis = response.json()

            st.success("Event analyzed successfully!")

        else:

            st.error("Failed to analyze event.")

    except Exception as e:
        st.error(e)
if st.session_state.analysis:

    st.subheader("📊 Event Analysis Result")

    analysis = st.session_state.analysis

    st.success("Event analyzed successfully!")

    st.write("**👤 Name:**", analysis["name"])
    st.write("**💼 Profession:**", analysis["profession"])
    st.write("**🎯 Interests:**", ", ".join(analysis["interests"]))
    st.write("**📅 Event:**", analysis["event"])
    st.write("**📝 Summary:**", analysis["summary"])
    st.write("**🤝 Networking Goal:**", analysis["networking_goal"])
# --------------------------------------------------
# Generate Conversation
# --------------------------------------------------

st.markdown("---")
st.header("💬 Generate Conversation")

if st.button("🚀 Generate Conversation"):

    if not name or not profession or not interests or not event_name:

        st.warning("Please complete the Event Analysis details first.")

    else:

        payload = {
            "name": name,
            "profession": profession,
            "interests": [
                i.strip()
                for i in interests.split(",")
            ],
            "event_name": event_name
        }

        try:

            response = requests.post(
                f"{API_URL}/generate-conversation",
                json=payload
            )

            if response.status_code == 200:

                data = response.json()

                st.write(data)

                st.session_state.conversation = data["conversation"]

                st.success("Conversation generated successfully!")

            else:

                st.error("Failed to generate conversation.")
        except Exception as e:
            st.error(e)
if st.session_state.conversation:

    st.subheader("🤖 AI Conversation")

    with st.container(border=True):
        st.markdown(st.session_state.conversation)

# --------------------------------------------------
# Fact Checker
# --------------------------------------------------

st.markdown("---")
st.header("🔎 Fact Checker")

query = st.text_area(
    "Enter networking advice or statement",
    placeholder="Example: Always personalize your introduction when meeting new people."
)

if st.button("✅ Fact Check"):

    if query.strip() == "":
        st.warning("Please enter some text to verify.")

    else:

        try:

            response = requests.post(
                f"{API_URL}/fact-check",
                json={
                    "query": query
                }
            )

            if response.status_code == 200:

                data = response.json()

                st.session_state.fact_result = data["summary"]

            else:

                st.error("Fact checking failed.")

        except Exception as e:

            st.error(e)

if st.session_state.fact_result:

    st.subheader("📋 Fact Check Result")

    st.write(st.session_state.fact_result)
# ==========================================
# 📂 Conversation History View
# ==========================================

st.divider()

st.header("📂 Conversation History")

if st.button("📜 Show History"):

    try:
        response = requests.get(f"{API_URL}/history")

        if response.status_code == 200:
            history = response.json()

            if history:
                for item in reversed(history):
                    st.markdown("---")
                    st.subheader("👤 Profile")
                    st.write(item["profile"])

                    st.subheader("💬 Conversation")
                    st.write(item["conversation"])
            else:
                st.info("No conversation history found.")

        else:
            st.error("Failed to load history.")

    except Exception as e:
        st.error(f"Error: {e}")
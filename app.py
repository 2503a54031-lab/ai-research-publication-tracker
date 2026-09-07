import streamlit as st
import pandas as pd
import plotly.express as px

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="AI Research Tracker",
    page_icon="🔬",
    layout="wide"
)

# =========================================================
# TITLE
# =========================================================

st.title("🔬 AI-Assisted Research Project & Publication Tracker")

st.write(
    "Welcome to your research management dashboard. "
    "Track projects, research papers, publications and deadlines."
)

st.divider()

# =========================================================
# DASHBOARD STATISTICS
# =========================================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="📁 Total Projects",
        value=5
    )

with col2:
    st.metric(
        label="🔬 Active Projects",
        value=3
    )

with col3:
    st.metric(
        label="📚 Research Papers",
        value=18
    )

with col4:
    st.metric(
        label="📝 Publications",
        value=4
    )

st.divider()

# =========================================================
# PROJECT PROGRESS
# =========================================================

st.subheader("📊 Research Project Progress")

project_data = pd.DataFrame({
    "Project": [
        "AI Disease Prediction",
        "Cybersecurity Detection",
        "Smart Agriculture",
        "IoT Security",
        "NLP Research"
    ],

    "Progress": [
        80,
        65,
        50,
        35,
        25
    ]
})

fig = px.bar(
    project_data,
    x="Project",
    y="Progress",
    text="Progress",
    title="Project Completion (%)"
)

fig.update_traces(
    texttemplate="%{text}%",
    textposition="outside"
)

fig.update_layout(
    yaxis=dict(range=[0, 100]),
    height=400
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =========================================================
# TWO COLUMN SECTION
# =========================================================

left_column, right_column = st.columns(2)

# =========================================================
# PUBLICATION STATUS
# =========================================================

with left_column:

    st.subheader("📝 Publication Status")

    publication_data = pd.DataFrame({
        "Status": [
            "Draft",
            "Submitted",
            "Under Review",
            "Accepted",
            "Published"
        ],

        "Number": [
            4,
            3,
            5,
            2,
            4
        ]
    })

    publication_chart = px.pie(
        publication_data,
        names="Status",
        values="Number",
        hole=0.4,
        title="Publication Overview"
    )

    st.plotly_chart(
        publication_chart,
        use_container_width=True
    )

# =========================================================
# UPCOMING DEADLINES
# =========================================================

with right_column:

    st.subheader("📅 Upcoming Deadlines")

    deadlines = pd.DataFrame({
        "Task": [
            "Literature Review",
            "Paper Submission",
            "Project Review",
            "Final Report"
        ],

        "Deadline": [
            "10 Sep 2026",
            "15 Sep 2026",
            "20 Sep 2026",
            "30 Sep 2026"
        ],

        "Priority": [
            "High",
            "High",
            "Medium",
            "Low"
        ]
    })

    st.dataframe(
        deadlines,
        use_container_width=True,
        hide_index=True
    )

# =========================================================
# AI ASSISTANT
# =========================================================

st.divider()

st.subheader("🤖 AI Research Assistant")

ai1, ai2, ai3 = st.columns(3)

with ai1:

    st.info(
        "💡 **Research Topic Generator**\n\n"
        "Generate research topic ideas based on your research area."
    )

with ai2:

    st.info(
        "📄 **Paper Summarizer**\n\n"
        "Upload a research paper and get an AI-assisted summary."
    )

with ai3:

    st.info(
        "🔎 **Research Gap Assistant**\n\n"
        "Analyze existing research and identify possible research gaps."
    )

# =========================================================
# RECENT ACTIVITY
# =========================================================

st.divider()

st.subheader("🕒 Recent Research Activity")

activity = pd.DataFrame({
    "Activity": [
        "Research paper added",
        "New AI research topic generated",
        "Project progress updated",
        "Publication status updated"
    ],

    "Date": [
        "07 Sep 2026",
        "06 Sep 2026",
        "05 Sep 2026",
        "04 Sep 2026"
    ],

    "Status": [
        "Completed",
        "Completed",
        "Updated",
        "Updated"
    ]
})

st.dataframe(
    activity,
    use_container_width=True,
    hide_index=True
)

# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "AI-Assisted Research Project and Publication Tracker "
    "| Developed using Python & Streamlit"
)

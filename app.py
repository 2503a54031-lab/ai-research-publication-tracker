import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------

st.set_page_config(
    page_title="Research Dashboard",
    page_icon="🔬",
    layout="wide"
)

# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------

st.markdown("""
<style>

.main-title {
    font-size: 36px;
    font-weight: 700;
    margin-bottom: 5px;
}

.subtitle {
    font-size: 17px;
    margin-bottom: 25px;
}

.card {
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #dddddd;
    background-color: #ffffff;
    text-align: center;
}

.card-title {
    font-size: 16px;
    font-weight: 600;
}

.card-value {
    font-size: 32px;
    font-weight: 700;
    margin-top: 8px;
}

.section-title {
    font-size: 24px;
    font-weight: 650;
    margin-top: 25px;
    margin-bottom: 15px;
}

</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------

st.markdown(
    '<div class="main-title">🔬 AI-Assisted Research Tracker</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Manage your research projects, papers, publications and deadlines in one place.'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# ---------------------------------------------------------
# SAMPLE DASHBOARD DATA
# ---------------------------------------------------------
# These are temporary values.
# Later we will get them automatically from SQLite.

total_projects = 5
active_projects = 3
total_papers = 18
published_papers = 4


# ---------------------------------------------------------
# STATISTICS CARDS
# ---------------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="📁 Total Projects",
        value=total_projects
    )

with col2:
    st.metric(
        label="🚀 Active Projects",
        value=active_projects
    )

with col3:
    st.metric(
        label="📚 Research Papers",
        value=total_papers
    )

with col4:
    st.metric(
        label="🏆 Published",
        value=published_papers
    )


st.markdown(
    '<div class="section-title">📊 Research Overview</div>',
    unsafe_allow_html=True
)


# ---------------------------------------------------------
# PROJECT PROGRESS DATA
# ---------------------------------------------------------

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


# ---------------------------------------------------------
# PROJECT PROGRESS CHART
# ---------------------------------------------------------

fig_progress = px.bar(
    project_data,
    x="Progress",
    y="Project",
    orientation="h",
    text="Progress",
    title="Research Project Progress"
)

fig_progress.update_traces(
    texttemplate="%{text}%",
    textposition="outside"
)

fig_progress.update_layout(
    xaxis_title="Progress (%)",
    yaxis_title="",
    xaxis=dict(range=[0, 100]),
    height=400
)

st.plotly_chart(
    fig_progress,
    use_container_width=True
)


# ---------------------------------------------------------
# TWO COLUMN SECTION
# ---------------------------------------------------------

left, right = st.columns(2)


# ---------------------------------------------------------
# PUBLICATION STATUS
# ---------------------------------------------------------

with left:

    st.subheader("📝 Publication Status")

    publication_data = pd.DataFrame({
        "Status": [
            "Draft",
            "Submitted",
            "Under Review",
            "Accepted",
            "Published"
        ],

        "Count": [
            4,
            3,
            5,
            2,
            4
        ]
    })

    fig_publication = px.pie(
        publication_data,
        names="Status",
        values="Count",
        hole=0.4
    )

    fig_publication.update_layout(
        height=400
    )

    st.plotly_chart(
        fig_publication,
        use_container_width=True
    )


# ---------------------------------------------------------
# UPCOMING DEADLINES
# ---------------------------------------------------------

with right:

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


# ---------------------------------------------------------
# AI ASSISTANT SECTION
# ---------------------------------------------------------

st.markdown(
    '<div class="section-title">🤖 AI Research Assistant</div>',
    unsafe_allow_html=True
)

ai_col1, ai_col2, ai_col3 = st.columns(3)

with ai_col1:

    st.info(
        "💡 Research Topics\n\n"
        "Generate research topic ideas using AI."
    )

with ai_col2:

    st.info(
        "📄 Paper Summarizer\n\n"
        "Summarize research papers using AI."
    )

with ai_col3:

    st.info(
        "🔎 Research Gaps\n\n"
        "Identify possible research gaps."
    )


# ---------------------------------------------------------
# RECENT RESEARCH ACTIVITY
# ---------------------------------------------------------

st.markdown(
    '<div class="section-title">🕒 Recent Research Activity</div>',
    unsafe_allow_html=True
)

activity_data = pd.DataFrame({
    "Activity": [
        "New research paper added",
        "AI topic generated",
        "Project progress updated",
        "Publication status changed"
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
    activity_data,
    use_container_width=True,
    hide_index=True
)


# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.divider()

st.caption(
    "🔬 AI-Assisted Research Project and Publication Tracker | "
    "Built with Python & Streamlit"
)

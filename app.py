import streamlit as st
import pandas as pd
import plotly.express as px
from database.database import get_connection


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Research Dashboard",
    page_icon="🔬",
    layout="wide"
)


# =========================================================
# HEADER
# =========================================================

st.title("🔬 AI-Assisted Research Project & Publication Tracker")

st.write(
    "A centralized dashboard to manage research projects, "
    "papers, publications and deadlines."
)

st.divider()


# =========================================================
# DATABASE CONNECTION
# =========================================================

connection = get_connection()


# =========================================================
# DASHBOARD COUNTS
# =========================================================

# Total Projects

total_projects = pd.read_sql_query(
    """
    SELECT COUNT(*) AS count
    FROM projects
    """,
    connection
).iloc[0]["count"]


# Active Projects

active_projects = pd.read_sql_query(
    """
    SELECT COUNT(*) AS count
    FROM projects
    WHERE status IN (
        'In Progress',
        'Active',
        'Ongoing'
    )
    """,
    connection
).iloc[0]["count"]


# Total Research Papers

total_papers = pd.read_sql_query(
    """
    SELECT COUNT(*) AS count
    FROM papers
    """,
    connection
).iloc[0]["count"]


# Published Papers

published_papers = pd.read_sql_query(
    """
    SELECT COUNT(*) AS count
    FROM publications
    WHERE status = 'Published'
    """,
    connection
).iloc[0]["count"]


# =========================================================
# STATISTICS CARDS
# =========================================================

col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "📁 Total Projects",
        int(total_projects)
    )


with col2:

    st.metric(
        "🚀 Active Projects",
        int(active_projects)
    )


with col3:

    st.metric(
        "📄 Research Papers",
        int(total_papers)
    )


with col4:

    st.metric(
        "🏆 Published",
        int(published_papers)
    )


st.divider()


# =========================================================
# PROJECT PROGRESS
# =========================================================

st.subheader("📊 Research Project Progress")


project_data = pd.read_sql_query(
    """
    SELECT
        title AS Project,
        progress AS Progress
    FROM projects
    ORDER BY id DESC
    """,
    connection
)


if not project_data.empty:

    project_chart = px.bar(
        project_data,
        x="Project",
        y="Progress",
        text="Progress",
        title="Project Completion"
    )

    project_chart.update_traces(
        texttemplate="%{text}%",
        textposition="outside"
    )

    project_chart.update_layout(
        yaxis=dict(
            title="Progress (%)",
            range=[0, 100]
        ),
        xaxis_title="Research Project",
        height=400
    )

    st.plotly_chart(
        project_chart,
        use_container_width=True
    )

else:

    st.info(
        "No research projects available. "
        "Add your first project from the Projects page."
    )


st.divider()


# =========================================================
# TWO COLUMN AREA
# =========================================================

left_column, right_column = st.columns(2)


# =========================================================
# PUBLICATION STATUS
# =========================================================

with left_column:

    st.subheader("📝 Publication Status")

    publication_data = pd.read_sql_query(
        """
        SELECT
            status AS Status,
            COUNT(*) AS Number
        FROM publications
        GROUP BY status
        ORDER BY Number DESC
        """,
        connection
    )


    if not publication_data.empty:

        publication_chart = px.pie(
            publication_data,
            names="Status",
            values="Number",
            hole=0.45,
            title="Publication Overview"
        )

        st.plotly_chart(
            publication_chart,
            use_container_width=True
        )

    else:

        st.info(
            "No publication records available yet."
        )


# =========================================================
# UPCOMING DEADLINES
# =========================================================

with right_column:

    st.subheader("📅 Upcoming Deadlines")

    deadline_data = pd.read_sql_query(
        """
        SELECT
            task AS Task,
            related_project AS Project,
            deadline AS Deadline,
            priority AS Priority,
            status AS Status
        FROM deadlines
        WHERE status != 'Completed'
        ORDER BY deadline ASC
        LIMIT 5
        """,
        connection
    )


    if not deadline_data.empty:

        st.dataframe(
            deadline_data,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.info(
            "No upcoming deadlines."
        )


st.divider()


# =========================================================
# RESEARCH SUMMARY
# =========================================================

st.subheader("📚 Research Summary")


summary_col1, summary_col2, summary_col3 = st.columns(3)


# Papers this year

current_year = pd.Timestamp.now().year

papers_this_year = pd.read_sql_query(
    """
    SELECT COUNT(*) AS count
    FROM papers
    WHERE year = ?
    """,
    connection,
    params=(current_year,)
).iloc[0]["count"]


# Submitted publications

submitted_publications = pd.read_sql_query(
    """
    SELECT COUNT(*) AS count
    FROM publications
    WHERE status = 'Submitted'
    """,
    connection
).iloc[0]["count"]


# Under review

under_review = pd.read_sql_query(
    """
    SELECT COUNT(*) AS count
    FROM publications
    WHERE status = 'Under Review'
    """,
    connection
).iloc[0]["count"]


with summary_col1:

    st.metric(
        "📅 Papers This Year",
        int(papers_this_year)
    )


with summary_col2:

    st.metric(
        "📤 Submitted",
        int(submitted_publications)
    )


with summary_col3:

    st.metric(
        "🔍 Under Review",
        int(under_review)
    )


st.divider()


# =========================================================
# RECENT RESEARCH PAPERS
# =========================================================

st.subheader("📄 Recent Research Papers")


recent_papers = pd.read_sql_query(
    """
    SELECT
        title AS Title,
        authors AS Authors,
        year AS Year,
        venue AS Venue
    FROM papers
    ORDER BY id DESC
    LIMIT 5
    """,
    connection
)


if not recent_papers.empty:

    st.dataframe(
        recent_papers,
        use_container_width=True,
        hide_index=True
    )

else:

    st.info(
        "No research papers added yet."
    )


st.divider()


# =========================================================
# RECENT PUBLICATIONS
# =========================================================

st.subheader("🏆 Recent Publications")


recent_publications = pd.read_sql_query(
    """
    SELECT
        paper_title AS Paper,
        venue AS Venue,
        status AS Status,
        submission_date AS Submitted
    FROM publications
    ORDER BY id DESC
    LIMIT 5
    """,
    connection
)


if not recent_publications.empty:

    st.dataframe(
        recent_publications,
        use_container_width=True,
        hide_index=True
    )

else:

    st.info(
        "No publication records available."
    )


# =========================================================
# CLOSE DATABASE
# =========================================================

connection.close()


# =========================================================
# AI ASSISTANT SECTION
# =========================================================

st.divider()

st.subheader("🤖 AI Research Assistant")


ai_col1, ai_col2, ai_col3 = st.columns(3)


with ai_col1:

    st.info(
        """
        ### 💡 Research Topic Generator

        Generate new research topic ideas
        based on your research area.
        """
    )


with ai_col2:

    st.info(
        """
        ### 📄 Paper Summarizer

        Upload a research paper and
        generate an AI-assisted summary.
        """
    )


with ai_col3:

    st.info(
        """
        ### 🔎 Research Gap Assistant

        Analyze existing research and
        identify possible research gaps.
        """
    )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "AI-Assisted Research Project and Publication Tracker "
    "| Python • Streamlit • SQLite • AI"
)

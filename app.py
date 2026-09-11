import streamlit as st
import sqlite3

# ---------------- DATABASE ----------------
conn = sqlite3.connect("research_tracker.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    researcher TEXT,
    status TEXT,
    progress INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS publications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    journal TEXT,
    status TEXT,
    year INTEGER
)
""")

conn.commit()

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Research Tracker",
    page_icon="🔬",
    layout="wide"
)

# ---------------- SIDEBAR ----------------
st.sidebar.title("🔬 Research Tracker")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Research Projects",
        "Publications",
        "AI Assistant",
        "Analytics"
    ]
)

# ---------------- DASHBOARD ----------------
if page == "Dashboard":

    st.title("🔬 AI-Assisted Research Project & Publication Tracker")

    st.write(
        "Manage research projects, publications and research progress "
        "using a simple AI-assisted dashboard."
    )

    projects = cursor.execute(
        "SELECT * FROM projects"
    ).fetchall()

    publications = cursor.execute(
        "SELECT * FROM publications"
    ).fetchall()

    total_projects = len(projects)
    total_publications = len(publications)

    completed = sum(
        1 for p in projects if p[3] == "Completed"
    )

    in_progress = sum(
        1 for p in projects if p[3] == "In Progress"
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("📁 Projects", total_projects)
    col2.metric("🚀 In Progress", in_progress)
    col3.metric("📚 Publications", total_publications)
    col4.metric("✅ Completed", completed)

    st.markdown("---")

    st.subheader("📊 Research Overview")

    if projects:
        for project in projects:
            st.write(f"### {project[1]}")
            st.write(f"Researcher: {project[2]}")
            st.write(f"Status: {project[3]}")
            st.progress(project[4] / 100)
            st.write(f"Progress: {project[4]}%")
    else:
        st.info("No research projects added yet.")

# ---------------- PROJECTS ----------------
elif page == "Research Projects":

    st.title("📁 Research Projects")

    with st.form("project_form"):

        title = st.text_input("Project Title")
        researcher = st.text_input("Researcher / Team")

        status = st.selectbox(
            "Project Status",
            ["Planning", "In Progress", "Completed", "On Hold"]
        )

        progress = st.slider(
            "Progress",
            0,
            100,
            50
        )

        submit = st.form_submit_button("➕ Add Project")

        if submit:

            if title and researcher:

                cursor.execute(
                    """
                    INSERT INTO projects
                    (title, researcher, status, progress)
                    VALUES (?, ?, ?, ?)
                    """,
                    (title, researcher, status, progress)
                )

                conn.commit()

                st.success("Project added successfully!")

            else:
                st.warning("Please enter project title and researcher.")

    st.markdown("---")

    projects = cursor.execute(
        "SELECT * FROM projects"
    ).fetchall()

    for project in projects:

        with st.container(border=True):

            st.subheader(project[1])

            st.write(
                f"👨‍🔬 Researcher: {project[2]}"
            )

            st.write(
                f"📌 Status: {project[3]}"
            )

            st.progress(project[4] / 100)

            st.write(
                f"Progress: {project[4]}%"
            )

# ---------------- PUBLICATIONS ----------------
elif page == "Publications":

    st.title("📚 Publications")

    with st.form("publication_form"):

        title = st.text_input("Publication Title")

        journal = st.text_input(
            "Journal / Conference"
        )

        status = st.selectbox(
            "Publication Status",
            [
                "Draft",
                "Under Review",
                "Accepted",
                "Published"
            ]
        )

        year = st.number_input(
            "Publication Year",
            2000,
            2100,
            2026
        )

        submit = st.form_submit_button(
            "➕ Add Publication"
        )

        if submit:

            if title:

                cursor.execute(
                    """
                    INSERT INTO publications
                    (title, journal, status, year)
                    VALUES (?, ?, ?, ?)
                    """,
                    (title, journal, status, year)
                )

                conn.commit()

                st.success(
                    "Publication added successfully!"
                )

            else:
                st.warning(
                    "Please enter publication title."
                )

    st.markdown("---")

    publications = cursor.execute(
        "SELECT * FROM publications"
    ).fetchall()

    for publication in publications:

        with st.container(border=True):

            st.subheader(publication[1])

            st.write(
                f"📖 Journal: {publication[2]}"
            )

            st.write(
                f"📌 Status: {publication[3]}"
            )

            st.write(
                f"📅 Year: {publication[4]}"
            )

# ---------------- AI ASSISTANT ----------------
elif page == "AI Assistant":

    st.title("🤖 AI Research Assistant")

    topic = st.text_input(
        "Enter your research topic"
    )

    if st.button("✨ Generate Suggestions"):

        if topic:

            st.success(
                "AI-assisted research suggestions"
            )

            st.subheader("💡 Suggested Research Plan")

            st.write(
                f"Research Topic: **{topic}**"
            )

            st.write("1. Identify the research problem.")
            st.write("2. Review existing research papers.")
            st.write("3. Find the research gap.")
            st.write("4. Select suitable methodology.")
            st.write("5. Collect and analyse data.")
            st.write("6. Prepare research results.")
            st.write("7. Prepare the publication.")

        else:
            st.warning(
                "Please enter a research topic."
            )

# ---------------- ANALYTICS ----------------
elif page == "Analytics":

    st.title("📈 Research Analytics")

    projects = cursor.execute(
        "SELECT * FROM projects"
    ).fetchall()

    publications = cursor.execute(
        "SELECT * FROM publications"
    ).fetchall()

    if projects:

        average = sum(
            p[4] for p in projects
        ) / len(projects)

    else:
        average = 0

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Average Progress",
        f"{average:.1f}%"
    )

    col2.metric(
        "Total Projects",
        len(projects)
    )

    col3.metric(
        "Total Publications",
        len(publications)
    )

    st.markdown("---")

    st.subheader("📊 Project Status")

    statuses = [
        "Planning",
        "In Progress",
        "Completed",
        "On Hold"
    ]

    for status in statuses:

        count = sum(
            1 for p in projects
            if p[3] == status
        )

        st.write(
            f"**{status}: {count}**"
        )

st.markdown("---")

st.caption(
    "AI-Assisted Research Project and Publication Tracker | "
    "Python + Streamlit + SQLite"
)

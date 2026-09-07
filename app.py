import streamlit as st
from database.database import create_tables

# Create database tables
create_tables()

st.set_page_config(
    page_title="AI Research Tracker",
    page_icon="🔬",
    layout="wide"
)

st.title("🔬 AI-Assisted Research Project and Publication Tracker")

st.write("""
Welcome to the AI-Assisted Research Project and Publication Tracker.

Use the sidebar to manage:

📊 Dashboard  
📁 Research Projects  
📄 Research Papers  
🤖 AI Research Assistant  
📝 Publications  
📅 Deadlines
""")

st.success("Database connected successfully!")

st.info("Select a page from the sidebar to get started.")

import streamlit as st
from service.Tasks import TaskService
from streamlit_extras.tags import tagger_component
#inituiate the app
st.set_page_config(
    page_title="Pentesting Notes App",
    page_icon="📝",
    layout="wide"
)

st.title("Pentesting Notes App")

# Create a session state object
session_state = st.session_state

# Check if the 'expense_tracker' object exists in the session state
if 'taskservice' not in session_state:
    taskservice = TaskService()

# Display family members
st.header("Tasks")

name_column, status_column, phase_column, priority_column, tags_column = st.columns(5)
name_column.write("**Name**")
status_column.write("**Status**")
phase_column.write("**Phase**")
priority_column.write("**Priority**")
tags_column.write("**Tags**")

for task in taskservice.getTasks():
    name_column.write(task.name)
    status_column.write(task.status)
    phase_column.write(task.phase)
    priority_column.write(task.priority)

    all_tag_name = []
    all_tag_color = []
    if task.tags:
        for tag in task.tags:
            all_tag_name.append(tag.name)
            all_tag_color.append(tag.color)
        with tags_column:
            tagger_component("",all_tag_name,all_tag_color)
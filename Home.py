import streamlit as st
from service.tasks_service import TaskService
from streamlit_extras.tags import tagger_component
from streamlit_extras.switch_page_button import switch_page
from st_pages import show_pages_from_config

#inituiate the app
st.set_page_config(
    page_title="Pentesting Notes App",
    page_icon="📝",
    layout="wide"
)

st.title("Pentesting Notes App")

show_pages_from_config()

# Create a session state object
session_state = st.session_state

# Check if the 'expense_tracker' object exists in the session state
if 'taskservice' not in session_state:
    taskservice = TaskService()

# Display family members
st.header("Tasks")

name_column, status_column, phase_column, priority_column, tags_column, button_column = st.columns(6)
name_column.write("**Name**")
status_column.write("**Status**")
phase_column.write("**Phase**")
priority_column.write("**Priority**")
tags_column.write("**Tags**")
button_column.write("")

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
    
    with button_column:
        if st.button("Edit",key=task.name):
            session_state.current_task = task
            switch_page("edittask")

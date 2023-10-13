import streamlit as st
from service.tasks_service import TaskService
from streamlit_extras.switch_page_button import switch_page

#inituiate the app
st.set_page_config(
    page_title="Pentesting Notes App",
    page_icon="📝",
    layout="wide"
)


session_state = st.session_state

if 'current_task' not in session_state:
    switch_page("Home")

if 'taskservice' not in session_state:
   taskservice = TaskService()

st.write(session_state.current_task)
import streamlit as st
from service.tasks_service import TaskService
from service.tag_service import TagService
from enums.status import Status
from enums.phase import Phase
from enums.priority import Priority

#inituiate the app
st.set_page_config(
    page_title="Pentesting Notes App",
    page_icon="📝",
    layout="wide"
)


session_state = st.session_state

if 'taskservice' not in session_state:
   taskservice = TaskService()

if 'tagservice' not in session_state:
   tagservice = TagService()


st.text_input("Enter your Taskname", key="taskname")
st.text_input("Enter your Description", key="description")
st.selectbox(
   "Select the status of your task",
   [status.name for status in Status],
   index=0,
   placeholder="Select status...",
   key="status",
)
st.selectbox(
   "Select the phase of your task",
  [phase.name for phase in Phase],
   index=0,
   placeholder="Select phase...",
   key="phase",
)
st.selectbox(
   "Select the priority of your task",
    [priority.name for priority in Priority],
   index=0,
   placeholder="Select priority...",
   key="priority",
)
st.text_area(label="Enter your comment", key="comment")

st.multiselect('Tags',[tag for tag in tagservice.getTags()],
                key="tags",format_func=lambda tag: tag.name)


if st.button("Add Task", type="primary"):
   try:
      TaskService().addTask(st.session_state.taskname, st.session_state.description,
                              st.session_state.status, st.session_state.phase, 
                              st.session_state.priority, st.session_state.comment, 
                              st.session_state.tags)
      st.success('Task saved', icon="✅")
   except ValueError as e:
        st.error(str(e),icon="❌")



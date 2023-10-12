import streamlit as st
from service.Tasks import TaskService
from service.Tasks import Color
from streamlit_extras.tags import tagger_component
#inituiate the app
st.set_page_config(
    page_title="Pentesting Notes App",
    page_icon="📝",
    layout="wide"
)


session_state = st.session_state

if 'taskservice' not in session_state:
        taskservice = TaskService()

st.text_input("Enter your Tagname", key="tagname")

st.selectbox(
   "Select the color of your tag",
    [color.name for color in Color],
   index=0,
   placeholder="Select color...",
   key="color",
)


if st.button("Add Tag", type="primary"):
    TaskService().addTag(st.session_state.tagname, st.session_state.color)
    st.success('Tag saved', icon="✅")

all_tag_name = []
all_tag_color = []
for tag in taskservice.getTags():
    all_tag_name.append(tag.name)
    all_tag_color.append(tag.color)

tagger_component("",all_tag_name,all_tag_color)


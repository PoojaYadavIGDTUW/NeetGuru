import streamlit as st

from config import *
from utils.ui import load_css
from pages.home import show_home

st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout=LAYOUT,
    initial_sidebar_state="collapsed"
)

load_css()

show_home()
import streamlit as st

from config import *

from utils.ui import load_css

from pages.home import show_home

st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout="wide"
)

load_css()

show_home()
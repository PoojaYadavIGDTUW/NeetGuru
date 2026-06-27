import streamlit as st


def load_css():

    files=[
        "css/theme.css",
        "css/base.css",
        "css/layout.css",
        "css/components.css",
        "css/animations.css"
    ]

    css=""

    for file in files:

        with open(file) as f:

            css+=f.read()

    st.markdown(f"<style>{css}</style>",unsafe_allow_html=True)



def hero():

    st.markdown("""

<div class="hero">

<div class="logo">🩺</div>

<div class="title">

NEET Guru AI

</div>

<div class="subtitle">

Your Personal AI Teacher

</div>

</div>

""",unsafe_allow_html=True)



def subject_cards():

    st.markdown("""

<div class="subject-container">

<div class="subject">

<div class="icon">🧬</div>

<div class="subject-title">

Biology

</div>

</div>

<div class="subject">

<div class="icon">⚛</div>

<div class="subject-title">

Physics

</div>

</div>

<div class="subject">

<div class="icon">🧪</div>

<div class="subject-title">

Chemistry

</div>

</div>

</div>

""",unsafe_allow_html=True)
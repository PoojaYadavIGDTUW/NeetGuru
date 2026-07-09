import streamlit as st


def load_css():

    css_files = [
        "css/theme.css",
        "css/base.css",
        "css/layout.css",
        "css/components.css",
        "css/animations.css",
    ]

    css = ""

    for file in css_files:
        with open(file, encoding="utf-8") as f:
            css += f.read()

    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


def hero():

    st.markdown("""
    <div class="hero">

    <h1>🩺 NEET Guru AI</h1>

    <p>Your Personal AI Teacher</p>

    <p>Learn • Revise • Practice • Crack NEET</p>

    </div>
    """, unsafe_allow_html=True)


def subject_selector():

    st.subheader("📚 Choose Subject")

    subjects = {
        "🧬 Biology":"Biology",
        "⚛ Physics":"Physics",
        "🧪 Chemistry":"Chemistry"
    }

    selected = st.radio(

        "",

        list(subjects.keys()),

        horizontal=True,

        label_visibility="collapsed"

    )

    return subjects[selected]
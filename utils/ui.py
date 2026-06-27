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

    st.markdown(
        """
        <div class="hero">
            <h1>🩺 NEET Guru AI</h1>
            <p>Your Personal AI Teacher</p>
            <p>Learn • Revise • Practice • Crack NEET</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def subject_cards():

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div class="subject-card">
                <h2>🧬</h2>
                <h3>Biology</h3>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="subject-card">
                <h2>⚛</h2>
                <h3>Physics</h3>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            """
            <div class="subject-card">
                <h2>🧪</h2>
                <h3>Chemistry</h3>
            </div>
            """,
            unsafe_allow_html=True,
        )
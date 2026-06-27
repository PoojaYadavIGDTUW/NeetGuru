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


def subject_card(icon, title, subtitle, color):

    st.markdown(
        f"""
        <div class="subject-card">

            <div style="font-size:55px;">{icon}</div>

            <h3 style="color:{color}; margin-bottom:8px;">
                {title}
            </h3>

            <p>{subtitle}</p>

        </div>
        """,
        unsafe_allow_html=True,
    )

def subject_cards():

    col1, col2, col3 = st.columns(3)

    with col1:
        subject_card(
            "🧬",
            "Biology",
            "Botany • Zoology",
            "#16A34A"
        )

    with col2:
        subject_card(
            "⚛",
            "Physics",
            "Mechanics • Modern",
            "#2563EB"
        )

    with col3:
        subject_card(
            "🧪",
            "Chemistry",
            "Organic • Inorganic",
            "#F59E0B"
        )
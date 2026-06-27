import streamlit as st

from utils.ui import hero,subject_cards


def show_home():

    st.markdown('<div class="main-container">',unsafe_allow_html=True)

    hero()

    subject_cards()

    st.text_input(
        "",
        placeholder="Ask your NEET question..."
    )

    st.button(
        "🚀 Ask AI",
        use_container_width=True
    )

    st.markdown("</div>",unsafe_allow_html=True)
import streamlit as st

from utils.ui import hero, subject_cards


def show_home():

    hero()

    st.write("")

    subject_cards()

    st.write("")
    st.write("")

    question = st.text_input(
        "",
        placeholder="🔍 Ask any NEET doubt..."
    )

    ask = st.button(
        "🚀 Ask AI",
        use_container_width=True
    )

    if ask:

        if question.strip() == "":

            st.warning("Please enter your question.")

        else:

            st.success("AI integration will be connected in Sprint 3.")
import streamlit as st

from utils.ui import hero, subject_selector


def show_home():

    hero()

    st.write("")

    # ------------------------
    # Subject Selection
    # ------------------------

    subject = subject_selector()

    st.session_state["subject"] = subject

    st.success(f"📚 Selected Subject : {subject}")

    st.divider()

    # ------------------------
    # Search Box
    # ------------------------

    placeholder = f"Ask your {subject} question..."

    question = st.text_area(

        "",

        placeholder=placeholder,

        height=140

    )

    st.write("")

    col1, col2, col3 = st.columns([1,2,1])

    with col2:

        ask = st.button(

            "🚀 Ask AI",

            use_container_width=True,

            type="primary"

        )

    if ask:

        if question.strip() == "":

            st.warning("Please enter your question.")

            return

        st.session_state["question"] = question

        st.info("🤖 AI will answer in Sprint 3.")
import streamlit as st

from utils.ui import hero, subject_selector


def show_home():

    hero()

    st.write("")

    subject = subject_selector()

    st.success(f"Selected Subject : {subject}")

    st.write("")

    question = st.text_input(

        "",

        placeholder=f"Ask your {subject} question..."

    )

    col1,col2,col3 = st.columns([1,2,1])

    with col2:

        ask = st.button(

            "🚀 Ask AI",

            use_container_width=True

        )

    if ask:

        if question.strip()=="":

            st.warning("Please enter a question.")

        else:

            st.success("AI integration coming in Sprint 3.")
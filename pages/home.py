import streamlit as st

def show_home():

    st.markdown(
        """
        <div class="main-title">
        🩺 NEET Guru AI
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="subtitle">
        Your Personal AI Teacher
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("###")
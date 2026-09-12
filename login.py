import streamlit as st


def show_login():

    st.markdown(
        """
        <h1>
        SkillBridge AI
        </h1>

        <p>
        Human Capital Digital Twin Platform
        </p>
        """,
        unsafe_allow_html=True
    )


    st.subheader(
        "Select your role"
    )


    role = st.radio(
    "Select your role",
    [
        "Worker",
        "Enterprise"
    ],
    key="login_role"
)


    if st.button(
    "Login",
    key="login_button"):

        st.session_state["role"] = role

        st.session_state["logged_in"] = True

        st.rerun()
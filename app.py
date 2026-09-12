import streamlit as st


from components.layout import (
    render_header,
    render_sidebar
)

from login import show_login


st.set_page_config(

    page_title="SkillBridge AI",

    page_icon=None,

    layout="wide",

    initial_sidebar_state="expanded"

)



# =====================================
# MAIN APP
# =====================================


def main():


    # -----------------------------
    # SESSION
    # -----------------------------

    if "logged_in" not in st.session_state:

        st.session_state["logged_in"] = False



    # -----------------------------
    # LOGIN SCREEN
    # -----------------------------

    if not st.session_state["logged_in"]:

        show_login()

        return



    # -----------------------------
    # PLATFORM
    # -----------------------------


    render_header()


    selected_page = render_sidebar()



    if selected_page == "Dashboard":

        from views.dashboard import show_dashboard

        show_dashboard()



    elif selected_page == "Enterprise":

        from views.enterprise import show_enterprise

        show_enterprise()



    elif selected_page == "Matching":

        from views.matching import show_matching

        show_matching()



    elif selected_page == "Worker Twin":

        from views.worker_twin import show_worker_twin

        show_worker_twin()



    elif selected_page == "Community":

        from views.community import show_community

        show_community()



    elif selected_page == "Quality Control":

        from views.quality import show_quality

        show_quality()



    elif selected_page == "Trust & Safety":

        from views.trust import show_trust

        show_trust()



    elif selected_page == "ESG Impact":

        from views.impact import show_impact

        show_impact()



    # -----------------------------
    # DEMO LOGOUT
    # -----------------------------

    st.sidebar.divider()


    st.sidebar.write(
        f"Logged in as: {st.session_state['role']}"
    )


    if st.sidebar.button(
        "Logout"
    ):

        st.session_state["logged_in"] = False

        st.session_state["role"] = None

        st.rerun()





if __name__ == "__main__":

    main()
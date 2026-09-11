import streamlit as st

from components.theme import apply_global_style
from components.layout import render_sidebar, render_header


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(

    page_title="SkillBridge AI",

    page_icon=None,

    layout="wide",

    initial_sidebar_state="expanded"

)


# ==================================================
# GLOBAL STYLE
# ==================================================

apply_global_style()


# ==================================================
# HEADER
# ==================================================

render_header()


# ==================================================
# SIDEBAR NAVIGATION
# ==================================================

selected_page = render_sidebar()



# ==================================================
# PAGE ROUTING
# ==================================================


if selected_page == "Overview":

    from pages.dashboard import show_dashboard

    show_dashboard()



elif selected_page == "Worker Digital Twin":

    from pages.worker_twin import show_worker_twin

    show_worker_twin()



elif selected_page == "Enterprise Requests":

    from pages.enterprise import show_enterprise

    show_enterprise()



elif selected_page == "AI Matching":

    from pages.matching import show_matching

    show_matching()



elif selected_page == "Community Hub":

    from pages.community import show_community

    show_community()



elif selected_page == "Quality Control":

    from pages.quality import show_quality

    show_quality()



elif selected_page == "Impact Analytics":

    from pages.impact import show_impact

    show_impact()

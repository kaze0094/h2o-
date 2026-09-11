import streamlit as st


from components.layout import (
    render_header,
    render_sidebar
)



st.set_page_config(

    page_title="SkillBridge AI",

    page_icon=None,

    layout="wide",

    initial_sidebar_state="expanded"

)



def main():


    render_header()


    selected_page = render_sidebar()



    if selected_page == "Overview":

        from pages.dashboard import show_dashboard

        show_dashboard()



    elif selected_page == "Enterprise Request":

        from pages.enterprise import show_enterprise

        show_enterprise()



    elif selected_page == "AI Matching":

        from pages.matching import show_matching

        show_matching()



    elif selected_page == "Worker Digital Twin":

        from pages.worker_twin import show_worker_twin

        show_worker_twin()



    elif selected_page == "Community Hub":

        from pages.community import show_community

        show_community()



    elif selected_page == "Quality Control":

        from pages.quality import show_quality

        show_quality()



    elif selected_page == "Trust & Safety":

        from pages.trust import show_trust

        show_trust()



    elif selected_page == "ESG Impact":

        from pages.impact import show_impact

        show_impact()



if __name__ == "__main__":

    main()
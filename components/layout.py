import streamlit as st


def render_header():

    st.markdown(
        """
        <div style="
            display:flex;
            justify-content:space-between;
            align-items:center;
            padding-bottom:20px;
            border-bottom:1px solid #E5E7EB;
            margin-bottom:25px;
        ">

            <div>

                <div style="
                    font-size:28px;
                    font-weight:700;
                    color:#0F172A;
                ">
                    SkillBridge AI
                </div>


                <div style="
                    font-size:14px;
                    color:#64748B;
                    margin-top:5px;
                ">
                    Human Capital Digital Twin Platform
                </div>


            </div>


            <div style="
                text-align:right;
                font-size:13px;
                color:#64748B;
            ">

                AI-powered Inclusive Workforce Intelligence
                <br>
                Vietnam - China Pilot Network

            </div>


        </div>
        """,
        unsafe_allow_html=True
    )



def render_sidebar():

    with st.sidebar:


        st.markdown(
            """
            <div style="
                font-size:24px;
                font-weight:700;
                margin-bottom:5px;
            ">
                SkillBridge AI
            </div>


            <div style="
                font-size:12px;
                color:#CBD5E1;
                margin-bottom:30px;
            ">
                Human Capital Digital Twin
            </div>

            """,
            unsafe_allow_html=True
        )


        menu = st.radio(

            "Navigation",

            [
                "Overview",

                "Worker Digital Twin",

                "Enterprise Requests",

                "AI Matching",

                "Community Hub",

                "Quality Control",

                "Impact Analytics"

            ]

        )


        st.markdown(
            """
            <br>

            <div style="
                border-top:1px solid rgba(255,255,255,0.2);
                padding-top:15px;
                font-size:12px;
                color:#CBD5E1;
            ">

            System Status

            <br><br>

            AI Engine:
            <span style="color:#4ADE80;">
            Online
            </span>


            <br>

            Data Pipeline:
            <span style="color:#4ADE80;">
            Active
            </span>

            </div>

            """,
            unsafe_allow_html=True
        )


    return menu



def page_title(title, subtitle=None):

    st.markdown(
        f"""
        <div style="margin-bottom:25px;">

            <h1 style="
                font-size:32px;
                margin-bottom:5px;
            ">
                {title}
            </h1>

        """,
        unsafe_allow_html=True
    )


    if subtitle:

        st.markdown(
            f"""
            <div style="
                color:#64748B;
                font-size:15px;
            ">
                {subtitle}
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


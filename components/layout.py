import streamlit as st



def render_header():


    st.markdown(

    """

    <div style="
    padding:20px 0;
    ">

    <h1 style="
    color:#0F172A;
    font-size:36px;
    margin-bottom:5px;
    ">

    SkillBridge AI

    </h1>


    <p style="
    color:#475569;
    font-size:18px;
    ">

    Human Capital Digital Twin Platform

    </p>


    <p style="
    color:#64748B;
    ">

    AI-powered workforce intelligence
    for inclusive economic participation.

    </p>


    </div>

    """,

    unsafe_allow_html=True

    )




def render_sidebar():


    st.sidebar.markdown(

        """

        ## SkillBridge AI

        ---

        """

    )


    page = st.sidebar.radio(

        "Navigation",

        [

        "Overview",

        "Enterprise Request",

        "AI Matching",

        "Worker Digital Twin",

        "Community Hub",

        "Quality Control",

        "Trust & Safety",

        "ESG Impact"

        ]

    )


    st.sidebar.markdown(

        """

        ---

        ### Platform Status


        AI Engine:

        Online


        Verification:

        Active


        ESG Tracking:

        Enabled

        """

    )


    return page



def section_title(title, subtitle=None):


    st.markdown(

        f"""

        <h2 style="
        color:#0F172A;
        margin-top:25px;
        ">

        {title}

        </h2>

        """,

        unsafe_allow_html=True

    )


    if subtitle:

        st.caption(subtitle)





def metric_card(title,value):


    st.markdown(

        f"""

        <div style="
        background:#F8FAFC;
        padding:20px;
        border-radius:12px;
        border:1px solid #E2E8F0;
        ">


        <p style="
        color:#64748B;
        margin:0;
        ">

        {title}

        </p>


        <h2 style="
        color:#0F172A;
        ">

        {value}

        </h2>


        </div>

        """,

        unsafe_allow_html=True

    )
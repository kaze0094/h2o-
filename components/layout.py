import streamlit as st


# =====================================================
# GLOBAL THEME
# =====================================================

def load_theme():

    st.markdown(
        """
        <style>

        .stApp {

            background:#F8FAFC;

        }


        .block-container {

            padding-top:2rem;

            padding-left:3rem;

            padding-right:3rem;

        }


        h1,h2,h3,h4 {

            color:#102A43;

            font-family:Arial,sans-serif;

        }


        p,div,span {

            font-family:Arial,sans-serif;

        }



        /* CARD */

        .custom-card {

            background:white;

            border:1px solid #E2E8F0;

            border-radius:18px;

            padding:22px;

            box-shadow:
            0 4px 15px rgba(15,23,42,0.05);

        }



        .card-title {

            color:#64748B;

            font-size:14px;

        }



        .card-value {

            color:#102A43;

            font-size:30px;

            font-weight:700;

            margin-top:10px;

        }



        .card-desc {

            color:#94A3B8;

            font-size:13px;

            margin-top:8px;

        }



        /* SECTION */

        .section-title {

            color:#102A43;

            font-size:26px;

            font-weight:700;

            margin-top:30px;

        }


        .section-desc {

            color:#64748B;

            font-size:14px;

            margin-bottom:15px;

        }



        </style>

        """,

        unsafe_allow_html=True

    )



# =====================================================
# HEADER
# =====================================================


def render_header(

        title="SkillBridge AI",

        subtitle="Human Capital Digital Twin Platform"

):

    load_theme()


    st.markdown(

        f"""
<div style="
background:linear-gradient(135deg,#102A43,#2563EB);
padding:35px;
border-radius:20px;
color:white;
margin-bottom:30px;
">

<h1 style="
color:white;
font-size:42px;
margin:0;
">
{title}
</h1>


<p style="
color:white;
font-size:18px;
margin-top:20px;
">
{subtitle}
</p>


</div>
""",

        unsafe_allow_html=True

    )



page_header = render_header



# =====================================================
# SIDEBAR
# =====================================================


def render_sidebar():


    with st.sidebar:


        st.markdown(

            """

            <h2 style="
            color:#102A43;
            ">
            SkillBridge AI
            </h2>


            <p style="
            color:#64748B;
            ">
            Human Capital Digital Twin
            </p>

            """,

            unsafe_allow_html=True

        )


        st.divider()


        selected = st.radio(

            "Navigation",

            [

                "Dashboard",

                "Community",

                "Enterprise",

                "ESG Impact",

                "Matching",

                "Quality Control",

                "Trust & Safety",

                "Worker Twin"

            ]

        )


    return selected



# =====================================================
# SECTION TITLE
# =====================================================


def section_title(

        title,

        description=""

):


    st.markdown(

        f"""

        <div class="section-title">

        {title}

        </div>


        <div class="section-desc">

        {description}

        </div>

        """,

        unsafe_allow_html=True

    )



# =====================================================
# KPI CARD
# =====================================================


def metric_card(

        title,

        value,

        description=""

):


    st.markdown(

        f"""

        <div class="custom-card">


        <div class="card-title">

        {title}

        </div>


        <div class="card-value">

        {value}

        </div>


        <div class="card-desc">

        {description}

        </div>


        </div>

        """,

        unsafe_allow_html=True

    )



# =====================================================
# ENTERPRISE CARD
# =====================================================


def enterprise_card(

        title,

        content

):


    st.markdown(

        f"""

        <div class="custom-card">


        <h3>

        {title}

        </h3>


        <p style="
        color:#64748B;
        ">

        {content}

        </p>


        </div>

        """,

        unsafe_allow_html=True

    )



# =====================================================
# STATUS BADGE
# =====================================================


def status_badge(text):


    st.markdown(

        f"""

        <span style="
        background:#DCFCE7;
        color:#166534;
        padding:6px 14px;
        border-radius:20px;
        font-size:12px;
        font-weight:600;
        ">

        {text}

        </span>

        """,

        unsafe_allow_html=True

    )



# =====================================================
# LEGACY SUPPORT
# =====================================================


def page_title(

        title,
        subtitle="",
):
    section_title(title, subtitle)



    import streamlit as st


def premium_card(title, value):

    st.markdown(
        f"""
        <div style="
            background:white;
            border:1px solid #E2E8F0;
            border-radius:18px;
            padding:22px;
            height:120px;
        ">

            <div style="
                color:#64748B;
                font-size:14px;
            ">
                {title}
            </div>


            <div style="
                color:#102A43;
                font-size:30px;
                font-weight:700;
                margin-top:12px;
            ">
                {value}
            </div>


        </div>
        """,
        unsafe_allow_html=True
    )
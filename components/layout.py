import streamlit as st


# =====================================================
# GLOBAL STYLE SYSTEM
# =====================================================

def load_enterprise_theme():

    st.markdown(

        """

<style>


/* Main background */

.main {

    background-color:#F7F9FC;

}



/* Remove default padding */

.block-container {

    padding-top:2rem;

    padding-left:3rem;

    padding-right:3rem;

}



/* Typography */

h1,h2,h3 {

    color:#172B4D;

    font-family:
    "Inter",
    sans-serif;

}


p,span,div {

    font-family:
    "Inter",
    sans-serif;

}



/* KPI CARD */

.kpi-card {


    background:white;

    border-radius:14px;

    padding:22px;

    border:1px solid #E5E7EB;

    box-shadow:
    0 2px 8px rgba(0,0,0,0.04);


}



.kpi-title {


    color:#64748B;

    font-size:14px;

}


.kpi-value {


    margin-top:8px;

    font-size:32px;

    font-weight:700;

    color:#0F172A;


}



/* Section */

.section-title {


    font-size:24px;

    font-weight:700;

    margin-bottom:4px;


}



.section-description {


    color:#64748B;

    font-size:14px;

    margin-bottom:25px;


}



/* Enterprise card */

.enterprise-card {


    background:white;

    padding:24px;

    border-radius:16px;

    border:
    1px solid #E2E8F0;


}



.badge {


    display:inline-block;

    padding:
    5px 12px;

    border-radius:20px;

    background:#DCFCE7;

    color:#166534;

    font-size:12px;

    font-weight:600;


}



</style>


        """,

        unsafe_allow_html=True

    )



# =====================================================
# PAGE HEADER
# =====================================================


def page_header(
        title,
        subtitle=""
):


    st.markdown(

        f"""

<div>

<h1 style="
margin-bottom:5px;
">

{title}

</h1>


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


<div class="section-description">

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

<div class="kpi-card">


<div class="kpi-title">

{title}

</div>


<div class="kpi-value">

{value}

</div>


<div style="
color:#64748B;
font-size:13px;
margin-top:8px;
">

{description}

</div>


</div>


""",

        unsafe_allow_html=True

    )



# =====================================================
# ENTERPRISE BOX
# =====================================================


def enterprise_card(

        title,

        content

):


    st.markdown(

        f"""

<div class="enterprise-card">


<h3>

{title}

</h3>


<div>

{content}

</div>


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

<span class="badge">

{text}

</span>

""",

        unsafe_allow_html=True

    )
import streamlit as st
from services.trust_intelligence_service import (
    get_trust_intelligence
)

from services.trust_service import (
    get_entity_trust
)



def show_trust():


    # =========================
    # STYLE
    # =========================

    st.markdown(
        """

<style>


.hero {

background:
linear-gradient(
135deg,
#102A43,
#2563EB
);

padding:35px;

border-radius:20px;

color:white;

margin-bottom:30px;

}


.hero h1 {

font-size:36px;

margin:0;

}



.card {

background:white;

border:1px solid #E2E8F0;

border-radius:18px;

padding:22px;

height:120px;

}



.label {

color:#64748B;

font-size:14px;

}



.value {

color:#102A43;

font-size:30px;

font-weight:700;

margin-top:10px;

}



.section {

font-size:25px;

font-weight:700;

color:#102A43;

margin-top:35px;

margin-bottom:15px;

}



.layer-card {

background:white;

border:1px solid #E2E8F0;

border-radius:16px;

padding:20px;

margin-bottom:15px;

}



.insight {

background:#ECFDF5;

border-left:5px solid #22C55E;

padding:22px;

border-radius:14px;

color:#166534;

margin-top:25px;

}


</style>


""",

unsafe_allow_html=True
    )



    # =========================
    # HEADER
    # =========================


    st.markdown(
        """

<div class="hero">


<h1>
Trust & Safety Intelligence
</h1>


<p>
Verification system for enterprises and workforce reliability
</p>


</div>


""",

unsafe_allow_html=True
    )



    # =========================
    # DATA
    # =========================


    trust = get_entity_trust(
        "E001"
    )
    intel = get_trust_intelligence(
    "E001"
)

    if not trust:

        st.error(
            "Trust data unavailable"
        )

        return



    # =========================
    # KPI
    # =========================


    c1,c2,c3 = st.columns(3)



    with c1:

        st.markdown(
            """

<div class="card">


<div class="label">
Verification Status
</div>


<div class="value">
Verified
</div>


</div>


""",

unsafe_allow_html=True
        )



    with c2:

        st.markdown(

        f"""

<div class="card">


<div class="label">
Trust Score
</div>


<div class="value">
{trust["trust_score"]}
</div>


</div>


""",

unsafe_allow_html=True

        )



    with c3:

        st.markdown(

        """

<div class="card">


<div class="label">
Safety Status
</div>


<div class="value">
Active
</div>


</div>


""",

unsafe_allow_html=True

        )



    # =========================
    # TRUST FRAMEWORK
    # =========================


    st.markdown(

    """

<div class="section">

Trust Layer Analysis

</div>


""",

unsafe_allow_html=True

    )



    layers = [

        (
            "Enterprise Verification",
            "Business identity verification and organizational trust assessment."
        ),

        (
            "Workforce Verification",
            "Skill validation, performance history and reputation tracking."
        ),

        (
            "Transaction Protection",
            "Quality monitoring and completion tracking."
        )

    ]



    for title,desc in layers:


        st.markdown(

        f"""

<div class="layer-card">


<b>
{title}
</b>


<br><br>


<span style="
color:#64748B;
">

{desc}

</span>


</div>


""",

unsafe_allow_html=True

        )

    # =========================
    # AI TRUST INTELLIGENCE
    # =========================


    st.markdown(

    """

<div class="section">

AI Trust Intelligence

</div>

""",

    unsafe_allow_html=True

    )



    if intel:


        c1,c2 = st.columns(2)



        with c1:

            st.markdown(

            f"""

<div class="card">


<div class="label">

Trust Level

</div>


<div class="value">

{intel["trust_level"]}

</div>


</div>

""",

            unsafe_allow_html=True

            )



        with c2:

            st.markdown(

            f"""

<div class="card">


<div class="label">

Risk Level

</div>


<div class="value">

{intel["risk_level"]}

</div>


</div>

""",

            unsafe_allow_html=True

            )



        st.markdown(

        """

<div class="section">

Verification Signals

</div>

""",

        unsafe_allow_html=True

        )



        for signal in intel["signals"]:

            st.success(

                "✓ " + signal

            )

    # =========================
    # AI INSIGHT
    # =========================


    st.markdown(

    """

<div class="insight">


<b>
AI Insight
</b>


SkillBridge AI establishes a trusted operating
layer by combining verification, reliability
assessment and transaction monitoring.


</div>


""",

unsafe_allow_html=True

    )
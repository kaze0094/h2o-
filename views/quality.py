import streamlit as st
import pandas as pd


from services.quality_service import (
    get_project
)


from core.risk_engine import (
    calculate_project_risk
)



def show_quality():


    # ==================================
    # STYLE
    # ==================================

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


.hero h1{

font-size:36px;

margin:0;

}



.card{

background:white;

border:1px solid #E2E8F0;

border-radius:18px;

padding:22px;

height:120px;

}



.label{

font-size:14px;

color:#64748B;

}



.value{

font-size:30px;

font-weight:700;

color:#102A43;

margin-top:10px;

}



.section{

font-size:25px;

font-weight:700;

color:#102A43;

margin-top:35px;

margin-bottom:15px;

}



.insight{

background:#ECFDF5;

border-left:5px solid #22C55E;

padding:22px;

border-radius:14px;

color:#166534;

margin-top:25px;

}



.status{

background:#F8FAFC;

border:1px solid #E2E8F0;

border-radius:16px;

padding:25px;

}



.progress-bg{

background:#E5E7EB;

height:12px;

border-radius:10px;

overflow:hidden;

}



</style>

""",

unsafe_allow_html=True

)



    # ==================================
    # HEADER
    # ==================================


    st.markdown(

    """

<div class="hero">


<h1>
Quality Control Intelligence
</h1>


<p>
AI-powered production assurance and workforce performance monitoring
</p>


</div>

""",

unsafe_allow_html=True

)



    # ==================================
    # DATA
    # ==================================


    project = get_project(
        "P001"
    )


    if not project:

        st.error(
            "Project unavailable"
        )

        return



    risk = calculate_project_risk(
        project
    )



    # ==================================
    # KPI
    # ==================================


    c1,c2,c3 = st.columns(3)



    with c1:

        st.markdown(

        f"""

<div class="card">


<div class="label">
Completion
</div>


<div class="value">
{project["progress"]}%
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
Quality Score
</div>


<div class="value">
{project["quality_score"]}%
</div>


</div>

""",

unsafe_allow_html=True

)



    with c3:


        st.markdown(

        f"""

<div class="card">


<div class="label">
Risk Level
</div>


<div class="value">
{risk["risk"]}
</div>


</div>

""",

unsafe_allow_html=True

)




    # ==================================
    # PRODUCTION ASSURANCE
    # ==================================


    st.markdown(

    """

<div class="section">

Production Assurance

</div>

""",

unsafe_allow_html=True

)



    progress = project["progress"]



    st.markdown(

    f"""

<div class="status">


<b>
Production Completion
</b>


<br><br>


<div class="progress-bg">

<div style="
width:{progress}%;
height:12px;
background:#2563EB;
border-radius:10px;
">

</div>

</div>


<br>


Completion:

<b>
{progress}%
</b>


<br><br>


Defect Rate:

<b>
{project["defect_rate"]}%

</b>


<br><br>


AI Assessment:

<b>
{risk["risk"]} Risk

</b>


</div>


""",

unsafe_allow_html=True

)



    # ==================================
    # QUALITY METRICS
    # ==================================


    st.markdown(

    """

<div class="section">

Quality Performance Analysis

</div>

""",

unsafe_allow_html=True

)



    quality_df = pd.DataFrame(

    {

    "Metric":

    [

    "Completion",

    "Quality Score",

    "Defect Rate"

    ],


    "Value":

    [

    f'{project["progress"]}%',

    f'{project["quality_score"]}%',

    f'{project["defect_rate"]}%'

    ]

    }

    )



    st.dataframe(

        quality_df,

        hide_index=True,

        use_container_width=True

    )



    # ==================================
    # AI INSIGHT
    # ==================================


    st.markdown(

    f"""

<div class="insight">


<b>
AI Insight
</b>


<br><br>


Production quality assessment:

<b>
{risk["risk"]}
</b>


<br>


Workforce performance data indicates
the project is currently within acceptable
quality control parameters.


</div>


""",

unsafe_allow_html=True

)
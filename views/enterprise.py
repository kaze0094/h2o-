from services.workforce_matching_service import (
    generate_workforce_recommendation
)
import streamlit as st
import pandas as pd


from services.enterprise_service import get_enterprise
from services.job_service import get_job



def show_enterprise():


    # =========================
    # LOAD DATA
    # =========================

    enterprise = get_enterprise("E001")

    job = get_job("J001")


    if not enterprise or not job:

        st.error(
            "Enterprise data unavailable"
        )

        return



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

        margin-bottom:25px;

    }


    .hero h1 {

        margin:0;

        font-size:36px;

    }


    .hero p {

        font-size:16px;

        opacity:.9;

    }



    .card {

        background:white;

        border:1px solid #E2E8F0;

        border-radius:18px;

        padding:22px;

        min-height:120px;

    }


    .label {

        color:#64748B;

        font-size:14px;

    }


    .value {

        color:#102A43;

        font-size:28px;

        font-weight:700;

        margin-top:10px;

    }



    .section {

        font-size:26px;

        font-weight:700;

        color:#102A43;

        margin-top:35px;

        margin-bottom:15px;

    }



    .profile {

        background:white;

        border:1px solid #E2E8F0;

        border-radius:18px;

        padding:25px;

    }



    .insight {

        background:#ECFDF5;

        border-left:

        5px solid #22C55E;

        padding:22px;

        border-radius:14px;

        color:#166534;

        margin-top:30px;

    }


    </style>


    """,

    unsafe_allow_html=True
    )



    # =========================
    # HERO
    # =========================


    st.markdown(
    f"""

    <div class="hero">

    <h1>
    Enterprise Intelligence Console
    </h1>

    <p>
    Convert business demand into an AI-optimized workforce requirement
    </p>


    </div>

    """,

    unsafe_allow_html=True
    )



    # =========================
    # KPI
    # =========================


    c1,c2,c3,c4 = st.columns(4)


    kpis = [

        (
        "Enterprise",
        enterprise["name"]
        ),

        (
        "Trust Score",
        enterprise["trust_score"]
        ),

        (
        "Verification",
        "Verified"
        ),

        (
        "Workers Required",
        job["required_workers"]
        )

    ]



    for col,item in zip(
        [c1,c2,c3,c4],
        kpis
    ):

        with col:

            st.markdown(
            f"""

            <div class="card">

            <div class="label">
            {item[0]}
            </div>


            <div class="value">
            {item[1]}
            </div>


            </div>


            """,

            unsafe_allow_html=True
            )



    # =========================
    # ENTERPRISE PROFILE
    # =========================


    st.markdown(
    "<div class='section'>Enterprise Profile</div>",
    unsafe_allow_html=True
    )


    st.markdown(
    f"""

    <div class="profile">


    <b>
    {enterprise["name"]}
    </b>


    <p>
    Trust Score:
    {enterprise["trust_score"]}
    </p>


    <p>
    Status:
    Verified Enterprise Partner
    </p>


    </div>

    """,

    unsafe_allow_html=True
    )



    # =========================
    # JOB DIGITAL TWIN
    # =========================


    st.markdown(
    "<div class='section'>Job Digital Twin</div>",
    unsafe_allow_html=True
    )



    job_df = pd.DataFrame(

        {

        "Parameter":[

            "Task",

            "Production Quantity",

            "Duration",

            "Workers Required",

            "Required Skills"

        ],


        "Value":[

            job["task"],

            f'{job["quantity"]:,} units',

            job["duration"],

            job["required_workers"],

            ", ".join(job["required_skills"])

        ]

        }

    )


    st.dataframe(

        job_df,

        hide_index=True,

        use_container_width=True

    )

# =========================
# AI WORKFORCE RECOMMENDATION
# =========================


st.markdown(

"<div class='section'>AI Workforce Recommendation</div>",

unsafe_allow_html=True

)



recommendation = generate_workforce_recommendation(

    "E001",

    "J001"

)



if recommendation:


    requirement = recommendation["requirement"]



    st.markdown(

    f"""

    <div class="profile">

    <b>
    Workforce Requirement
    </b>


    <p>
    Workers Needed:
    {requirement["workers_needed"]}
    </p>


    <p>
    Required Skills:
    {", ".join(requirement["skills"])}
    </p>


    <p>
    Quality Target:
    {requirement["quality"]}
    </p>


    </div>

    """,

    unsafe_allow_html=True

    )



    st.subheader(

        "Recommended Workforce"

    )


    ranking = recommendation["recommendations"]



    if ranking:


        recommendation_df = pd.DataFrame(

            [

                {

                "Worker":

                    item["name"],


                "AI Match":

                    f'{item["score"]}%',


                "AI Reason":

                    "; ".join(
                        item["explanation"]
                    )

                }


                for item in ranking

            ]

        )


        st.dataframe(

            recommendation_df,

            hide_index=True,

            use_container_width=True

        )

    # =========================
    # INSIGHT
    # =========================


    st.markdown(
    """

    <div class="insight">

    <b>
    AI Insight
    </b>

    Enterprise requirements have been transformed
    into a structured workforce intelligence profile
    ready for AI matching.


    </div>


    """,

    unsafe_allow_html=True
    )
import streamlit as st
import pandas as pd

from components.layout import page_title

from services.enterprise_service import (
    get_enterprise
)

from services.job_service import (
    get_job
)



def show_enterprise():


    page_title(

        "Enterprise Workforce Request",

        "Convert business demand into an AI-optimized workforce requirement"

    )


    # =====================================
    # LOAD DATA
    # =====================================


    enterprise_id = "E001"

    job_id = "J001"


    enterprise = get_enterprise(
        enterprise_id
    )


    job = get_job(
        job_id
    )



    if enterprise is None or job is None:

        st.error(
            "Enterprise or Job data unavailable"
        )

        return



    # =====================================
    # ENTERPRISE PROFILE
    # =====================================


    st.markdown(

        '<div class="section-title">Verified Enterprise Profile</div>',

        unsafe_allow_html=True

    )


    c1,c2 = st.columns(2)



    with c1:


        st.markdown(

            f"""

            <div class="sb-card">


            <div class="sb-card-title">

            Company

            </div>


            <h2>

            {enterprise["name"]}

            </h2>


            <p>

            Industry:

            <b>
            {enterprise["industry"]}
            </b>


            </p>


            <p>

            Verification:

            <b style="color:#16A34A">

            Verified

            </b>


            </p>


            </div>


            """,

            unsafe_allow_html=True

        )



    with c2:


        st.markdown(

            f"""

            <div class="sb-card">


            <div class="sb-card-title">

            Enterprise Trust Score

            </div>


            <div class="sb-card-value">

            {enterprise["trust_score"]}

            </div>


            <div class="sb-card-desc">

            Trusted partner

            </div>


            </div>


            """,

            unsafe_allow_html=True

        )



    st.write("")



    # =====================================
    # JOB DIGITAL TWIN
    # =====================================


    st.markdown(

        '<div class="section-title">Generated Job Digital Twin</div>',

        unsafe_allow_html=True

    )



    job_table = pd.DataFrame(

        {

        "Parameter":[

            "Task",

            "Quantity",

            "Duration",

            "Required Workers",

            "Quality Standard"

        ],


        "Value":[

            job["task"],

            f'{job["quantity"]} units',

            job["duration"],

            job["workers_required"],

            job["quality_standard"]

        ]

        }

    )


    st.dataframe(

        job_table,

        use_container_width=True,

        hide_index=True

    )



    # =====================================
    # AI TASK ANALYSIS
    # =====================================


    st.markdown(

        '<div class="section-title">AI Requirement Analysis</div>',

        unsafe_allow_html=True

    )


    analysis = pd.DataFrame(

        {

        "Factor":[

            "Required Skill",

            "Workforce Size",

            "Quality Level",

            "Time Constraint"

        ],


        "AI Assessment":[

            "Packaging + Quality Inspection",

            "30 workers",

            "Error <2%",

            "14 days"

        ]

        }

    )


    st.dataframe(

        analysis,

        use_container_width=True,

        hide_index=True

    )



    # =====================================
    # BUSINESS VALUE
    # =====================================


    st.markdown(

        '<div class="section-title">Business Impact</div>',

        unsafe_allow_html=True

    )


    c1,c2,c3 = st.columns(3)



    with c1:

        st.metric(

            "Traditional Hiring Time",

            "14-21 days"

        )



    with c2:

        st.metric(

            "SkillBridge Response",

            "24-48 hours"

        )



    with c3:

        st.metric(

            "Workforce Flexibility",

            "+40%"

        )

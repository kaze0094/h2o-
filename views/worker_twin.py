import streamlit as st
import pandas as pd


from services.worker_service import (
    get_worker_v2
)


from services.worker_ai_service import (
    get_worker_capability_summary,
    calculate_worker_readiness,
    get_worker_job_recommendations
)



def show_worker_twin():


    worker = get_worker_v2(
        "W001"
    )


    if not worker:

        st.error(
            "Worker profile unavailable"
        )

        return



    identity = worker["identity"]



    # =====================================
    # HEADER
    # =====================================

    st.markdown(
        """
        <div style="
        background:linear-gradient(135deg,#102A43,#2563EB);
        padding:35px;
        border-radius:20px;
        color:white;
        margin-bottom:30px;
        ">

        <h1 style="color:white;">
        Worker Digital Twin
        </h1>

        <p>
        AI-powered human capability intelligence profile
        </p>

        </div>
        """,

        unsafe_allow_html=True
    )



    # =====================================
    # IDENTITY
    # =====================================

    st.subheader(
        "Worker Identity"
    )


    c1,c2,c3,c4 = st.columns(4)


    with c1:
        st.metric(
            "Worker",
            identity["name"]
        )


    with c2:
        st.metric(
            "Location",
            identity["location"]
        )


    with c3:
        st.metric(
            "Community",
            identity["community_id"]
        )


    with c4:
        st.metric(
            "Experience",
            f'{worker["experience"]["years"]} years'
        )



    st.divider()



    # =====================================
    # READINESS
    # =====================================

    readiness = calculate_worker_readiness(
        "W001"
    )


    st.subheader(
        "AI Workforce Readiness"
    )


    st.markdown(
        f"""
        <div style="
        background:white;
        border:1px solid #E2E8F0;
        border-radius:16px;
        padding:20px;
        ">

        <div style="
        color:#64748B;
        ">
        Readiness Score
        </div>


        <div style="
        font-size:32px;
        font-weight:700;
        color:#2563EB;
        ">
        {readiness}%
        </div>


        </div>
        """,

        unsafe_allow_html=True
    )



    st.divider()



    # =====================================
    # CAPABILITY
    # =====================================

    st.subheader(
        "Capability Intelligence"
    )


    capabilities = get_worker_capability_summary(
        "W001"
    )



    for item in capabilities:


        st.markdown(
            f"""
            <div style="
            background:white;
            border:1px solid #E2E8F0;
            border-radius:16px;
            padding:20px;
            margin-bottom:15px;
            ">


            <h3 style="
            color:#102A43;
            ">
            {item["skill"]}
            </h3>


            <div style="
            display:flex;
            justify-content:space-between;
            padding:8px 0;
            ">

            <span style="color:#64748B;">
            Category
            </span>

            <b>
            {item["category"]}
            </b>

            </div>



            <div style="
            display:flex;
            justify-content:space-between;
            padding:8px 0;
            ">

            <span style="color:#64748B;">
            Capability Score
            </span>

            <b style="color:#2563EB;">
            {item["score"]}%
            </b>

            </div>



            <div style="
            display:flex;
            justify-content:space-between;
            padding:8px 0;
            ">

            <span style="color:#64748B;">
            Verified
            </span>

            <b style="color:#16A34A;">
            ✓ Verified
            </b>

            </div>


            </div>
            """,

            unsafe_allow_html=True
        )



        for evidence in item["evidence"]:

            st.markdown(
                f"""
                <div style="
                background:#F8FAFC;
                border-radius:10px;
                padding:12px;
                margin-bottom:8px;
                ">

                <span style="
                color:#64748B;
                ">
                Evidence
                </span>

                <br>

                ✓ {evidence}

                </div>
                """,

                unsafe_allow_html=True
            )



    st.divider()



    # =====================================
    # PERFORMANCE
    # =====================================


    st.subheader(
        "Performance Intelligence"
    )


    performance = worker["performance"]


    performance_items = [

        ("Quality", performance["quality"]),

        ("Completion", performance["completion"]),

        ("Feedback", performance["feedback"])

    ]



    for name,value in performance_items:


        st.markdown(
            f"""
            <div style="
            display:flex;
            justify-content:space-between;
            padding:12px;
            background:white;
            border:1px solid #E2E8F0;
            border-radius:12px;
            margin-bottom:8px;
            ">

            <span>
            {name}
            </span>


            <b style="
            color:#2563EB;
            ">
            {value}%
            </b>

            </div>
            """,

            unsafe_allow_html=True
        )



    st.divider()



    # =====================================
    # AI RECOMMENDATION
    # =====================================

    st.subheader(
        "AI Job Recommendation"
    )


    recommendations = get_worker_job_recommendations(
        "W001"
    )



    if recommendations:


        for item in recommendations:


            st.markdown(
                f"""
                <div style="
                background:white;
                border:1px solid #E2E8F0;
                border-radius:15px;
                padding:18px;
                margin-bottom:12px;
                ">

                <b>
                Skill:
                </b>
                {item["skill"]}

                <br><br>

                <b>
                Recommended Jobs:
                </b>
                {", ".join(item["job"])}

                <br><br>

                <b>
                Confidence:
                </b>

                <span style="
                color:#2563EB;
                font-weight:700;
                ">
                {item["confidence"]}%
                </span>


                </div>
                """,

                unsafe_allow_html=True
            )


    else:

        st.info(
            "No AI recommendation available."
        )



    st.success(
        """
        AI Insight:
        Worker profile demonstrates verified capability,
        strong reliability and readiness for enterprise workforce matching.
        """
    )
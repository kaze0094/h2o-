import streamlit as st
import pandas as pd


from services.matching_service import (
    get_matching_result,
    get_worker_ranking
)



def show_matching():


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

            margin-bottom:25px;

        }


        .hero h1 {

            margin:0;

            font-size:36px;

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

            color:#102A43;

            font-size:25px;

            font-weight:700;

            margin-top:35px;

            margin-bottom:15px;

        }


        .insight {

            background:#ECFDF5;

            border-left:

            5px solid #22C55E;

            padding:22px;

            border-radius:14px;

            color:#166534;

            margin-top:25px;

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
        AI Workforce Recommendation Engine
        </h1>


        <p>
        Explainable AI for trusted workforce allocation
        </p>


        </div>
        """,

        unsafe_allow_html=True
    )



    # ==================================
    # LOAD AI ENGINE
    # ==================================


    matching_result = get_matching_result()

    ranking_result = get_worker_ranking()



    # ==================================
    # KPI
    # ==================================


    c1,c2,c3 = st.columns(3)



    with c1:

        st.markdown(
            """
            <div class="card">

            <div class="label">
            Matching Engine
            </div>


            <div class="value">
            Ready
            </div>


            </div>
            """,

            unsafe_allow_html=True
        )



    with c2:

        count = len(ranking_result) if ranking_result else 0


        st.markdown(
            f"""
            <div class="card">

            <div class="label">
            Ranked Candidates
            </div>


            <div class="value">
            {count}
            </div>


            </div>
            """,

            unsafe_allow_html=True
        )



    with c3:


        confidence = 0


        if ranking_result:

            confidence = ranking_result[0].get(
                "score",
                0
            )


        st.markdown(
            f"""
            <div class="card">

            <div class="label">
            AI Confidence
            </div>


            <div class="value">
            {confidence}%
            </div>


            </div>
            """,

            unsafe_allow_html=True
        )



    # ==================================
    # MATCHING RESULT
    # ==================================


    st.markdown(
        """
        <div class="section">
        AI Matching Analysis
        </div>
        """,

        unsafe_allow_html=True
    )



    if matching_result:


     score = matching_result.get(
        "match_score",
        0
    )


    skill = matching_result.get(
        "skill_compatibility",
        0
    )


    availability = matching_result.get(
        "availability",
        0
    )


    reliability = matching_result.get(
        "reliability",
        0
    )


    completion = matching_result.get(
        "completion_probability",
        0
    )


    st.markdown(
        f"""
        <div class="rank-card">

        <h3>
        AI Workforce Recommendation Score
        </h3>


        <h1 style="
        color:#2563EB;
        ">
        {score}%
        </h1>


        Overall workforce compatibility

        </div>
        """,

        unsafe_allow_html=True
    )



    metrics = pd.DataFrame(

        {
            "Capability":
            [
                "Skill Compatibility",
                "Availability",
                "Reliability",
                "Completion Probability"
            ],

            "Score":
            [
                skill,
                availability,
                reliability,
                completion
            ]

        }

    )


    st.bar_chart(

        metrics.set_index(
            "Capability"
        )

    )



    st.markdown(
        """
        <div class="section">
        AI Explanation
        </div>
        """,

        unsafe_allow_html=True
    )


    explanation = matching_result.get(
        "explaining",
        matching_result.get(
            "explanation",
            []
        )
    )


    if explanation:


        for item in explanation:


            st.markdown(

            f"""
            <div class="rank-card">

            ✓ {item}

            </div>

            """,

            unsafe_allow_html=True

            )


    else:

        st.info(
            "AI matching engine is connected and waiting for enterprise requirements and workforce capability data."
        )



    # ==================================
    # WORKER RANKING
    # ==================================


    st.markdown(
        """
        <div class="section">
        Worker Capability Ranking
        </div>
        """,

        unsafe_allow_html=True
    )



    if ranking_result:


        ranking_df = pd.DataFrame(
            ranking_result
        )


        st.dataframe(
            ranking_df,
            hide_index=True,
            use_container_width=True
        )


    else:


        st.info(
            "No worker ranking data available yet."
        )



    # ==================================
    # AI INSIGHT
    # ==================================


    st.markdown(
        """
        <div class="insight">

        <b>
        AI Insight
        </b>

        Matching engine architecture is ready.
        Once enterprise demand and worker capability
        profiles are connected, AI will generate
        explainable workforce recommendations.

        </div>

        """,

        unsafe_allow_html=True
    )
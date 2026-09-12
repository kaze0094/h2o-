import streamlit as st
import pandas as pd


from services.matching_service import (
    get_matching_result
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


        .rank-card {

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

    matching_result = get_matching_result(
        "J001"
    )


    if matching_result:

        ranking_result = matching_result.get(
            "ranking",
            []
        )

    else:

        ranking_result = []



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

        st.markdown(
            f"""
            <div class="card">

            <div class="label">
            Ranked Candidates
            </div>

            <div class="value">
            {len(ranking_result)}
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

            <h1>
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



    # ==================================
    # AI EXPLANATION
    # ==================================

    st.markdown(
        """
        <div class="section">
        AI Explanation
        </div>
        """,
        unsafe_allow_html=True
    )


    explanation = []


    if matching_result:

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
            "AI explanation is not available."
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

            [

                {

                "Worker":
                item.get(
                    "name",
                    ""
                ),


                "Score":
                item.get(
                    "score",
                    0
                )

                }

                for item in ranking_result

            ]

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

        <br><br>

        Matching engine connects enterprise demand
        with verified workforce capability using
        explainable AI.

        </div>
        """,
        unsafe_allow_html=True
    )
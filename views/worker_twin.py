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


    # =====================================
    # HEADER
    # =====================================






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
    # READINESS SCORE
    # =====================================


    readiness = calculate_worker_readiness(

        "W001"

    )



    st.subheader(

        "AI Workforce Readiness"

    )


    st.metric(

        "Readiness Score",

        f"{readiness}%"

    )



    st.divider()



    # =====================================
    # CAPABILITY INTELLIGENCE
    # =====================================


    st.subheader(

        "Capability Intelligence"

    )


    capabilities = get_worker_capability_summary(

        "W001"

    )



    for item in capabilities:


        with st.container():


            st.markdown(

            f"""

            ### {item["skill"]}


            Category:

            {item["category"]}


            Capability Score:

            {item["score"]}%


            Verified:

            {item["verified"]}

            """,

            )



            evidence = pd.DataFrame(

                {

                    "Evidence":

                    item["evidence"]

                }

            )


            st.dataframe(

                evidence,

                hide_index=True,

                use_container_width=True

            )



    st.divider()



    # =====================================
    # PERFORMANCE
    # =====================================


    st.subheader(

        "Performance Intelligence"

    )


    performance = worker["performance"]



    performance_df = pd.DataFrame(

        {

            "Metric":

            [

                "Quality",

                "Completion",

                "Feedback"

            ],


            "Score":

            [

                performance["quality"],

                performance["completion"],

                performance["feedback"]

            ]

        }

    )


    st.dataframe(

        performance_df,

        hide_index=True,

        use_container_width=True

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


        rec_df = pd.DataFrame(

            [

                {

                    "Skill":

                    item["skill"],


                    "Recommended Jobs":

                    ", ".join(item["job"]),


                    "Confidence":

                    f'{item["confidence"]}%'

                }


                for item in recommendations

            ]

        )


        st.dataframe(

            rec_df,

            hide_index=True,

            use_container_width=True

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
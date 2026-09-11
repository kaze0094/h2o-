import streamlit as st
import pandas as pd

from components.layout import (
    section_title,
    metric_card
)

from services.job_service import (
    get_job
)

from services.worker_service import (
    get_all_workers
)

from services.matching_service import (
    match_workers,
    match_communities
)



def show_matching():


    section_title(

        "AI Workforce Recommendation Engine",

        "Explainable AI for trusted workforce allocation"

    )


    job = get_job(
        "J001"
    )


    workers = get_all_workers()


    # COMMUNITY MATCHING

    st.subheader(
        "Step 1 — Community Network Matching"
    )


    communities = match_communities()



    community_df = pd.DataFrame(

        communities

    )


    st.dataframe(

        community_df,

        hide_index=True,

        use_container_width=True

    )



    best = communities[0]



    st.success(

        f"""

        Recommended Workforce Hub:


        {best["community"]}


        AI Confidence:

        {best["score"]}%

        """

    )



    st.divider()



    # WORKER MATCHING


    st.subheader(

        "Step 2 — Worker Capability Ranking"

    )


    results = match_workers(

        job,

        workers

    )


    df = pd.DataFrame(

        [

            {

                "Worker":

                r["name"],


                "AI Match":

                f'{r["score"]}%'

            }


            for r in results

        ]

    )


    st.dataframe(

        df,

        hide_index=True,

        use_container_width=True

    )



    st.divider()



    # EXPLANATION


    if results:


        top = results[0]


        st.subheader(

            "Why AI Selected This Worker?"

        )


        explanation = pd.DataFrame(

            top["explanation"].items(),

            columns=[

                "Factor",

                "Score"

            ]

        )


        st.dataframe(

            explanation,

            hide_index=True,

            use_container_width=True

        )


        st.success(

            f"""

            Recommended Worker:


            {top["name"]}


            Overall Confidence:

            {top["score"]}%

            """

        )
import streamlit as st
import pandas as pd

from components.layout import page_title

from services.job_service import get_job

from services.worker_service import get_all_workers

from services.matching_service import run_matching



def show_matching():


    page_title(

        "AI Matching Engine",

        "Explainable AI workforce allocation"

    )


    job = get_job(
        "J001"
    )


    workers = get_all_workers()



    results = run_matching(

        job,

        workers

    )



    st.markdown(

        "### Ranked Workforce Recommendation"

    )



    table = pd.DataFrame(

        [

            {

            "Worker":

            r["worker_name"],


            "Match Score":

            f'{r["match_score"]}%'

            }

            for r in results

        ]

    )


    st.dataframe(

        table,

        use_container_width=True

    )



    if results:


        best = results[0]


        st.success(

            f"""

            Recommended:

            {best["worker_name"]}


            Match Score:

            {best["match_score"]}%

            """

        )


        st.markdown(

            "### Explainable AI"

        )


        explanation = pd.DataFrame(

            best["explanation"].items(),

            columns=[

                "Factor",

                "Score"

            ]

        )


        st.dataframe(

            explanation,

            use_container_width=True

        )

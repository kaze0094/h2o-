import streamlit as st
import pandas as pd

from components.layout import (
    section_title,
    metric_card
)

from services.enterprise_service import (
    get_enterprise
)

from services.job_service import (
    get_job
)


def show_enterprise():


    section_title(
        "Enterprise Workforce Request",
        "Convert business demand into an AI-optimized workforce requirement"
    )


    enterprise = get_enterprise(
        "E001"
    )


    job = get_job(
        "J001"
    )


    if not enterprise or not job:

        st.error(
            "Enterprise data unavailable"
        )

        return



    # Enterprise Overview

    c1,c2,c3 = st.columns(3)


    with c1:

        metric_card(
            "Enterprise",
            enterprise["name"]
        )


    with c2:

        metric_card(
            "Trust Score",
            str(
                enterprise["trust_score"]
            )
        )


    with c3:

        metric_card(
            "Verification",
            "Verified"
        )



    st.divider()


    section_title(
        "Job Digital Twin"
    )


    job_df = pd.DataFrame(

        {

        "Parameter":

        [

            "Task",

            "Quantity",

            "Duration",

            "Workers Required",

            "Required Skills"

        ],


        "Value":

        [

            job["task"],

            f'{job["quantity"]:,} units',

            job["duration"],

            job["required_workers"],

            ", ".join(
                job["required_skills"]
            )

        ]

        }

    )


    st.dataframe(

        job_df,

        hide_index=True,

        use_container_width=True

    )



    st.success(

        """
        AI has transformed enterprise demand
        into a structured workforce requirement.

        Ready for workforce intelligence matching.
        """

    )
import streamlit as st
import pandas as pd
import plotly.express as px

from components.layout import (
    section_title,
    metric_card
)

from services.worker_service import (
    get_worker,
    get_worker_profile
)


def show_worker_twin():

    section_title(
        "Worker Digital Twin",
        "AI-generated capability profile for inclusive workforce intelligence"
    )


    worker = get_worker(
        "W001"
    )


    if not worker:

        st.error(
            "Worker profile unavailable"
        )

        return



    # ==========================
    # BASIC PROFILE
    # ==========================


    st.subheader(
        "Capability Profile"
    )


    c1,c2,c3 = st.columns(3)


    with c1:

        metric_card(
            "Worker",
            worker["name"]
        )


    with c2:

        metric_card(
            "Location",
            worker["location"]
        )


    with c3:

        metric_card(
            "Verification",
            worker["trust"]["verification"]
        )


    st.divider()



    # ==========================
    # SKILLS
    # ==========================


    st.subheader(
        "Skill Intelligence"
    )


    skill_df = pd.DataFrame(

        {

            "Skill":

            list(
                worker["skills"].keys()
            ),


            "Score":

            list(
                worker["skills"].values()
            )

        }

    )


    fig = px.bar(

        skill_df,

        x="Score",

        y="Skill",

        orientation="h",

        title="Verified Capability Score"

    )


    st.plotly_chart(

        fig,

        use_container_width=True

    )



    # ==========================
    # PERFORMANCE
    # ==========================


    st.subheader(

        "Performance History"

    )


    performance = worker["performance"]


    c1,c2,c3,c4 = st.columns(4)


    with c1:

        metric_card(

            "Quality Score",

            f'{performance["quality_score"]}%'

        )


    with c2:

        metric_card(

            "Completion Rate",

            f'{performance["completion_rate"]}%'

        )


    with c3:

        metric_card(

            "Feedback",

            f'{performance["feedback_score"]}%'

        )


    with c4:

        metric_card(

            "Completed Tasks",

            performance["completed_tasks"]

        )



    st.divider()



    # ==========================
    # AI EXPLANATION
    # ==========================


    st.subheader(

        "AI Capability Interpretation"

    )


    st.info(

        f"""

        This worker is suitable for enterprise tasks because:


        • Verified skills match production requirements


        • Historical quality performance:

        {performance["quality_score"]}%


        • Task completion reliability:

        {performance["completion_rate"]}%


        • Trusted workforce status:

        {worker["trust"]["verification"]}


        """

    )
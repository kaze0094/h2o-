import streamlit as st
import pandas as pd
import plotly.express as px

from components.layout import page_title

from services.worker_service import (
    get_worker,
    get_worker_skills
)



def show_worker_twin():


    page_title(
        "Worker Digital Twin",
        "AI-generated capability profile based on verified skills and performance"
    )


    # ==========================
    # Load Worker Data
    # ==========================

    worker_id = "W001"


    worker = get_worker(worker_id)


    if worker is None:

        st.error(
            "Worker profile not found"
        )

        return



    skills = get_worker_skills(
        worker_id
    )


    skill_df = pd.DataFrame(

        {

            "Skill": list(
                skills.keys()
            ),

            "Score": list(
                skills.values()
            )

        }

    )


    # ==========================
    # PROFILE
    # ==========================


    st.markdown(

        f"""

        <div class="sb-card">

        <div class="sb-card-title">
        Worker Capability Profile
        </div>


        <h2>
        {worker["name"]}
        </h2>


        <p>
        Location:
        <b>{worker["location"]}</b>
        </p>


        <p>
        Availability:
        <b>{worker["availability"]}</b>
        </p>


        <p>
        Status:
        <b style="color:#16A34A">
        Verified
        </b>
        </p>


        </div>

        """,

        unsafe_allow_html=True

    )


    st.write("")


    # ==========================
    # SCORE
    # ==========================


    c1,c2,c3 = st.columns(3)


    with c1:

        st.metric(

            "Reliability Score",

            f'{worker["reliability"]}%'

        )


    with c2:

        st.metric(

            "Skill Categories",

            len(skills)

        )


    with c3:

        st.metric(

            "Experience",

            worker["experience"]

        )


    # ==========================
    # SKILLS
    # ==========================


    st.markdown(

        '<div class="section-title">Verified Skills</div>',

        unsafe_allow_html=True

    )


    fig = px.bar(

        skill_df,

        x="Score",

        y="Skill",

        orientation="h",

        template="plotly_white"

    )


    st.plotly_chart(

        fig,

        use_container_width=True

    )


    # ==========================
    # AI EXPLANATION
    # ==========================


    st.markdown(

        """

        <div class="sb-card">


        <h3>
        AI Capability Explanation
        </h3>


        <p>

        This worker is recommended because:


        <br><br>

        • Verified packaging skill

        <br>

        • High reliability history

        <br>

        • Suitable availability window

        <br>

        • Previous quality performance


        </p>


        </div>

        """,

        unsafe_allow_html=True

    )
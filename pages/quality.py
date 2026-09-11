import streamlit as st

from components.layout import (
    section_title,
    metric_card
)

from services.quality_service import (
    get_project
)

from core.risk_engine import (
    calculate_project_risk
)



def show_quality():


    section_title(

        "Quality Control Intelligence",

        "Monitor production quality through workforce performance data"

    )


    project = get_project(

        "P001"

    )


    if not project:

        st.error(
            "Project unavailable"
        )

        return



    risk = calculate_project_risk(

        project

    )



    c1,c2,c3 = st.columns(3)



    with c1:

        metric_card(

            "Completion",

            f'{project["progress"]}%'

        )


    with c2:

        metric_card(

            "Quality Score",

            f'{project["quality_score"]}%'

        )


    with c3:

        metric_card(

            "Risk Level",

            risk["risk"]

        )



    st.divider()



    st.subheader(

        "Production Assurance"

    )


    st.write(

        f"""

        Current production:

        {project["progress"]}% completed


        Defect rate:

        {project["defect_rate"]}%


        AI assessment:

        {risk["risk"]} risk

        """

    )
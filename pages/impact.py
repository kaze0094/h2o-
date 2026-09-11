import streamlit as st

from components.layout import (
    section_title,
    metric_card
)

from services.impact_service import (
    get_project_impact
)



def show_impact():


    section_title(

        "ESG Impact Analytics",

        "Generate measurable social impact evidence for enterprises"

    )


    impact = get_project_impact(

        "P001"

    )


    if not impact:

        st.error(
            "Impact data unavailable"
        )

        return



    c1,c2,c3 = st.columns(3)



    with c1:

        metric_card(

            "Workers Supported",

            impact["workers_supported"]

        )


    with c2:

        metric_card(

            "Working Hours",

            impact["working_hours"]

        )


    with c3:

        metric_card(

            "Income Generated",

            f'¥{impact["income_generated"]:,}'

        )



    st.divider()


    st.subheader(

        "SDG Contribution"

    )


    for sdg in impact["sdg"]:

        st.write(

            f"• {sdg}"

        )


    st.success(

        """

        SkillBridge AI provides measurable evidence

        of inclusive employment impact.

        """

    )
import streamlit as st

from components.layout import (
    section_title,
    metric_card
)

from services.community_service import (
    get_community
)


def show_community():


    section_title(

        "Community Workforce Intelligence",

        "Analyze verified workforce hubs and community production capability"

    )


    community = get_community(

        "C001"

    )


    if not community:

        st.error(
            "Community data unavailable"
        )

        return



    # ==========================
    # KPI OVERVIEW
    # ==========================


    c1, c2, c3, c4 = st.columns(4)


    with c1:

        metric_card(

            "Community",

            community["name"]

        )


    with c2:

        metric_card(

            "Worker Capacity",

            f'{community["worker_capacity"]:,}'

        )


    with c3:

        metric_card(

            "Production Capacity",

            f'{community["production_capacity"]:,}'

        )


    with c4:

        metric_card(

            "Verification",

            "Verified"

        )



    st.divider()



    # ==========================
    # COMMUNITY PROFILE
    # ==========================


    section_title(

        "Community Profile"

    )


    st.markdown(

        f"""

        **{community["name"]}**


        Location:

        {community["location"]}


        Status:

        {community["verification"]}

        """,

    )



    st.divider()



    # ==========================
    # PERFORMANCE INTELLIGENCE
    # ==========================


    section_title(

        "Workforce Performance Intelligence"

    )


    performance = community["performance"]



    p1, p2, p3 = st.columns(3)



    with p1:

        metric_card(

            "Quality Score",

            f'{performance["quality_score"]}%'

        )


    with p2:

        metric_card(

            "Completion Rate",

            f'{performance["completion_rate"]}%'

        )


    with p3:

        metric_card(

            "Reliability Score",

            f'{performance["reliability_score"]}%'

        )



    st.divider()



    # ==========================
    # AI INSIGHT
    # ==========================


    section_title(

        "AI Workforce Insight"

    )


    st.success(

        f"""

        Community hub {community["name"]}

        demonstrates strong workforce reliability

        with {performance["quality_score"]}% quality score

        and {performance["completion_rate"]}% completion rate.

        Ready for enterprise workforce matching.

        """

    )
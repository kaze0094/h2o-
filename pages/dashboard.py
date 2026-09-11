import streamlit as st
import pandas as pd

from components.layout import (
    section_title,
    metric_card
)

from services.worker_service import (
    get_all_workers
)

from services.enterprise_service import (
    get_enterprises
)

from services.quality_service import (
    get_projects
)

from services.impact_service import (
    get_impacts
)



def show_dashboard():


    section_title(

        "Executive Intelligence Dashboard",

        "Real-time overview of inclusive workforce ecosystem"

    )


    workers = get_all_workers()

    enterprises = get_enterprises()

    projects = get_projects()

    impacts = get_impacts()



    # =========================
    # KPI
    # =========================


    c1,c2,c3,c4 = st.columns(4)



    with c1:

        metric_card(

            "Verified Workers",

            len(workers)

        )


    with c2:

        metric_card(

            "Enterprise Partners",

            len(enterprises)

        )


    with c3:

        metric_card(

            "Active Projects",

            len(projects)

        )


    with c4:

        metric_card(

            "Social Impact",

            f'¥{impacts[0]["income_generated"]:,}'

        )



    st.divider()



    # =========================
    # PLATFORM VALUE
    # =========================


    section_title(
        "Platform Value Creation"
    )


    value = pd.DataFrame(

        {

        "Metric":[

            "Workforce Access",

            "Quality Assurance",

            "Business Flexibility",

            "Social Inclusion"

        ],


        "Impact":[

            "Connects invisible workforce",

            "AI verified capability",

            "Flexible production capacity",

            "Creates inclusive income"

        ]

        }

    )


    st.dataframe(

        value,

        hide_index=True,

        use_container_width=True

    )



    st.success(

        """
        SkillBridge AI transforms fragmented labor capacity
        into a trusted digital workforce network.
        """

    )
import streamlit as st
import pandas as pd


from components.layout import (
    section_title,
    metric_card
)


from services.impact_service import (
    get_project_impact
)


from services.esg_ai_service import (
    generate_esg_summary
)



def show_impact():



    # =========================
    # HEADER
    # =========================


    section_title(

        "ESG Impact Intelligence",

        "Generate measurable social impact evidence through inclusive workforce deployment"

    )



    # =========================
    # LOAD DATA
    # =========================


    impact = get_project_impact(

        "P001"

    )


    if not impact:


        st.error(

            "Impact data unavailable"

        )

        return



    esg = generate_esg_summary(

        "P001"

    )



    if not esg:


        st.error(

            "ESG analysis unavailable"

        )

        return




    # =========================
    # ESG KPI OVERVIEW
    # =========================


    c1,c2,c3,c4 = st.columns(4)



    with c1:


        metric_card(

            "Social Impact Score",

            f'{esg["score"]}%'

        )



    with c2:


        metric_card(

            "Workers Supported",

            impact["workers_supported"]

        )



    with c3:


        metric_card(

            "Working Hours",

            f'{impact["working_hours"]:,}'

        )



    with c4:


        metric_card(

            "Income Generated",

            f'¥{impact["income_generated"]:,}'

        )



    st.divider()




    # =========================
    # IMPACT PROFILE
    # =========================


    st.subheader(

        "Social Impact Profile"

    )



    impact_df = pd.DataFrame(

        [

            {

                "Dimension":
                "Employment Contribution",

                "Impact":
                f'{impact["workers_supported"]} workers supported'

            },


            {

                "Dimension":
                "Economic Contribution",

                "Impact":
                f'¥{impact["income_generated"]:,} generated income'

            },


            {

                "Dimension":
                "Workforce Participation",

                "Impact":
                f'{impact["working_hours"]:,} working hours'

            }

        ]

    )



    st.dataframe(

        impact_df,

        hide_index=True,

        use_container_width=True

    )




    st.divider()




    # =========================
    # SDG CONTRIBUTION
    # =========================


    st.subheader(

        "SDG Contribution"

    )



    sdg_df = pd.DataFrame(

        {

            "Sustainable Development Goals":

            impact["sdg"]

        }

    )



    st.dataframe(

        sdg_df,

        hide_index=True,

        use_container_width=True

    )




    st.divider()




    # =========================
    # AI ESG INSIGHT
    # =========================


    st.subheader(

        "AI ESG Insight"

    )


    st.success(

        esg["message"]

    )
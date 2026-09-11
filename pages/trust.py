import streamlit as st

from components.layout import (
    section_title,
    metric_card
)

from services.trust_service import (
    get_entity_trust
)



def show_trust():


    section_title(

        "Trust & Safety Infrastructure",

        "Verification system for enterprises and workforce reliability"

    )


    trust = get_entity_trust(

        "E001"

    )


    if not trust:

        st.error(
            "Trust data unavailable"
        )

        return



    c1,c2,c3 = st.columns(3)



    with c1:

        metric_card(

            "Verification",

            "Verified"

        )


    with c2:

        metric_card(

            "Trust Score",

            trust["trust_score"]

        )


    with c3:

        metric_card(

            "Safety Status",

            "Active"

        )



    st.divider()


    st.subheader(

        "Verification Framework"

    )


    st.write(

        """

        Enterprise verification:

        ✓ Business identity verification


        Workforce verification:

        ✓ Skill validation

        ✓ Performance history

        ✓ Reputation tracking


        Transaction protection:

        ✓ Quality monitoring

        ✓ Completion tracking

        """

    )
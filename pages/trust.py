import streamlit as st
import pandas as pd
import plotly.express as px

from components.layout import page_title



def show_trust():


    page_title(

        "Trust & Safety System",

        "Building reliable connections between enterprises, communities and workers"

    )


    # =================================
    # TRUST OVERVIEW
    # =================================


    st.markdown(
        '<div class="section-title">Trust Intelligence Overview</div>',
        unsafe_allow_html=True
    )


    c1,c2,c3,c4 = st.columns(4)


    metrics = [

        ("Verified Enterprises","328"),

        ("Verified Workers","12,580"),

        ("Fraud Detection Rate","99.2%"),

        ("Successful Projects","95%")

    ]


    for col,item in zip(
        [c1,c2,c3,c4],
        metrics
    ):

        with col:

            st.markdown(

                f"""

                <div class="sb-card">


                <div class="sb-card-title">

                {item[0]}

                </div>


                <div class="sb-card-value">

                {item[1]}

                </div>


                </div>

                """,

                unsafe_allow_html=True

            )



    st.write("")



    # =================================
    # ENTERPRISE VERIFICATION
    # =================================


    st.markdown(
        '<div class="section-title">Enterprise Verification</div>',
        unsafe_allow_html=True
    )


    enterprise = pd.DataFrame({

        "Company":[

            "ABC Manufacturing",

            "XYZ Electronics",

            "Green Product Co."

        ],

        "Business Verification":[

            100,

            100,

            95

        ],

        "Payment Reliability":[

            98,

            96,

            92

        ],

        "Trust Score":[

            96,

            94,

            91

        ]

    })


    st.dataframe(

        enterprise,

        use_container_width=True,

        hide_index=True

    )



    # =================================
    # RISK DETECTION
    # =================================


    st.markdown(
        '<div class="section-title">AI Risk Detection</div>',
        unsafe_allow_html=True
    )


    risks = pd.DataFrame({

        "Category":[

            "Suspicious Payment Request",

            "Unusual Salary Pattern",

            "Identity Verification"

        ],

        "Status":[

            "No Risk",

            "No Risk",

            "Verified"

        ]

    })


    st.dataframe(

        risks,

        use_container_width=True,

        hide_index=True

    )



    # =================================
    # TRUST MODEL
    # =================================


    st.markdown(
        '<div class="section-title">Trust Score Model</div>',
        unsafe_allow_html=True
    )


    trust = pd.DataFrame({

        "Factor":[

            "Verification",

            "Payment Reliability",

            "Project History",

            "Community Feedback"

        ],

        "Weight":[

            30,

            30,

            20,

            20

        ]

    })


    fig = px.pie(

        trust,

        names="Factor",

        values="Weight",

        title="Enterprise Trust Score Components"

    )


    fig.update_layout(

        template="plotly_white",

        height=350

    )


    st.plotly_chart(

        fig,

        use_container_width=True

    )
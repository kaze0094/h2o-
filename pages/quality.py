import streamlit as st
import pandas as pd
import plotly.express as px

from components.layout import page_title



def show_quality():


    page_title(

        "Quality Control Center",

        "AI-powered quality monitoring for distributed workforce production"

    )


    # =====================================
    # PROJECT OVERVIEW
    # =====================================


    st.markdown(
        '<div class="section-title">Active Production Project</div>',
        unsafe_allow_html=True
    )


    c1,c2,c3,c4 = st.columns(4)


    metrics = [

        ("Project","ABC Packaging"),

        ("Order Size","10,000 units"),

        ("Completion","72%"),

        ("Quality Confidence","96%")

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



    # =====================================
    # BATCH MONITORING
    # =====================================


    st.markdown(
        '<div class="section-title">Production Batch Monitoring</div>',
        unsafe_allow_html=True
    )


    batches = pd.DataFrame({

        "Batch":[

            "Batch 001",

            "Batch 002",

            "Batch 003",

            "Batch 004"

        ],

        "Quantity":[

            2500,

            2500,

            2500,

            2500

        ],

        "Status":[

            "Completed",

            "Completed",

            "Quality Review",

            "Processing"

        ],

        "Quality Score":[

            98,

            96,

            91,

            95

        ]

    })


    st.dataframe(

        batches,

        use_container_width=True,

        hide_index=True

    )



    # =====================================
    # QUALITY ANALYTICS
    # =====================================


    st.markdown(
        '<div class="section-title">AI Quality Analytics</div>',
        unsafe_allow_html=True
    )


    quality = pd.DataFrame({

        "Metric":[

            "Packaging Accuracy",

            "Completion Rate",

            "Worker Reliability",

            "Previous Quality"

        ],

        "Score":[

            97,

            94,

            95,

            96

        ]

    })


    fig = px.bar(

        quality,

        x="Metric",

        y="Score",

        title="Quality Intelligence Score"

    )


    fig.update_layout(

        template="plotly_white",

        height=350

    )


    st.plotly_chart(

        fig,

        use_container_width=True

    )



    # =====================================
    # AI RISK PREDICTION
    # =====================================


    st.markdown(
        '<div class="section-title">AI Quality Prediction</div>',
        unsafe_allow_html=True
    )


    st.markdown(

        """

        <div class="sb-card">


        <h3>

        Production Risk Assessment

        </h3>


        <p>

        Predicted final quality:

        <b>96%</b>

        </p>


        <p>

        Estimated defect rate:

        <b>1.8%</b>

        </p>


        <p>

        Delay probability:

        <b>Low</b>

        </p>


        <p style="
        color:#16A34A;
        font-weight:600;
        ">

        Recommendation:

        Continue current workforce allocation.

        </p>


        </div>

        """,

        unsafe_allow_html=True

    )



    # =====================================
    # FEEDBACK LOOP
    # =====================================


    st.markdown(
        '<div class="section-title">Continuous Learning Loop</div>',
        unsafe_allow_html=True
    )


    st.info(

        """
        Quality results continuously improve:

        Worker reliability score

        →

        AI matching accuracy

        →

        Future production quality

        """

    )
import streamlit as st
import pandas as pd
import plotly.express as px

from components.layout import page_title



def show_impact():


    page_title(

        "Impact Analytics",

        "Verified social impact measurement powered by workforce intelligence"

    )


    # =====================================
    # IMPACT KPI
    # =====================================


    st.markdown(

        '<div class="section-title">Social Impact Overview</div>',

        unsafe_allow_html=True

    )


    c1,c2,c3,c4 = st.columns(4)


    metrics = [

        ("Workers Supported","12,580"),

        ("Employment Hours","125,000"),

        ("Income Generated","¥8.6M"),

        ("Community Hubs","42")

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
    # SDG ALIGNMENT
    # =====================================


    st.markdown(

        '<div class="section-title">SDG Impact Alignment</div>',

        unsafe_allow_html=True

    )


    sdg = pd.DataFrame({

        "SDG":[

            "SDG 5 Gender Equality",

            "SDG 8 Decent Work",

            "SDG 10 Reduced Inequality"

        ],

        "Contribution":[

            90,

            95,

            88

        ]

    })


    fig = px.bar(

        sdg,

        x="SDG",

        y="Contribution",

        title="Impact Contribution Score"

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
    # COMPANY REPORT
    # =====================================


    st.markdown(

        '<div class="section-title">Enterprise Impact Report</div>',

        unsafe_allow_html=True

    )


    report = pd.DataFrame({

        "Indicator":[

            "Employment Created",

            "Workers Supported",

            "Income Generated",

            "Community Participation"

        ],

        "Result":[

            "3500 hours",

            "120 workers",

            "¥200,000",

            "3 communities"

        ]

    })


    st.dataframe(

        report,

        use_container_width=True,

        hide_index=True

    )



    # =====================================
    # IMPACT SCORE
    # =====================================


    st.markdown(

        '<div class="section-title">SkillBridge Impact Score</div>',

        unsafe_allow_html=True

    )


    st.markdown(

        """

        <div class="sb-card">


        <div class="sb-card-title">

        Overall Impact Score

        </div>


        <div class="sb-card-value">

        92 / 100

        </div>


        <p>

        Employment Creation:
        <b>95%</b>

        <br>

        Income Generation:
        <b>90%</b>

        <br>

        Inclusion:
        <b>94%</b>

        <br>

        Sustainability:
        <b>88%</b>

        </p>


        </div>

        """,

        unsafe_allow_html=True

    )
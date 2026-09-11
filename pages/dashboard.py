import streamlit as st
import pandas as pd
import plotly.express as px

from components.layout import page_title



def show_dashboard():


    page_title(
        "Workforce Intelligence Overview",
        "AI-powered Human Capital Digital Twin for inclusive workforce networks"
    )


    # ==================================================
    # MOCK DATA LAYER
    # Sau này thay bằng service layer
    # ==================================================


    workers = pd.DataFrame({

        "Region":[
            "Bac Ninh",
            "Thai Nguyen",
            "Hai Duong",
            "Quang Ninh"
        ],

        "Workers":[
            250,
            180,
            210,
            140
        ],

        "Certified":[
            180,
            120,
            150,
            95
        ]

    })


    demand = pd.DataFrame({

        "Month":[
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May"
        ],

        "Demand":[
            120,
            180,
            240,
            320,
            410
        ]

    })


    # ==================================================
    # KPI SECTION
    # ==================================================


    st.markdown(
        '<div class="section-title">Platform Performance</div>',
        unsafe_allow_html=True
    )


    c1,c2,c3,c4 = st.columns(4)


    with c1:

        st.markdown(
            """
            <div class="sb-card">

            <div class="sb-card-title">
            Active Workforce
            </div>

            <div class="sb-card-value">
            12,580
            </div>

            <div class="sb-card-desc">
            Verified workers
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    with c2:

        st.markdown(
            """
            <div class="sb-card">

            <div class="sb-card-title">
            Enterprise Requests
            </div>

            <div class="sb-card-value">
            328
            </div>

            <div class="sb-card-desc">
            Active projects
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    with c3:

        st.markdown(
            """
            <div class="sb-card">

            <div class="sb-card-title">
            AI Matching Accuracy
            </div>

            <div class="sb-card-value">
            94.6%
            </div>

            <div class="sb-card-desc">
            Average confidence
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    with c4:

        st.markdown(
            """
            <div class="sb-card">

            <div class="sb-card-title">
            Social Impact
            </div>

            <div class="sb-card-value">
            ¥8.6M
            </div>

            <div class="sb-card-desc">
            Income generated
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )



    st.write("")


    # ==================================================
    # COMMUNITY MAP + FORECAST
    # ==================================================


    left,right = st.columns([1,1])


    with left:


        st.markdown(
            '<div class="section-title">Community Workforce Network</div>',
            unsafe_allow_html=True
        )


        fig = px.bar(

            workers,

            x="Region",

            y="Workers",

            title="Verified Workforce by Region"

        )


        fig.update_layout(

            height=350,

            template="plotly_white",

            showlegend=False

        )


        st.plotly_chart(

            fig,

            use_container_width=True

        )



    with right:


        st.markdown(
            '<div class="section-title">AI Workforce Demand Forecast</div>',
            unsafe_allow_html=True
        )


        fig2 = px.line(

            demand,

            x="Month",

            y="Demand",

            markers=True,

            title="Projected Enterprise Workforce Demand"

        )


        fig2.update_layout(

            height=350,

            template="plotly_white"

        )


        st.plotly_chart(

            fig2,

            use_container_width=True

        )



    # ==================================================
    # AI RECOMMENDATION
    # ==================================================


    st.markdown(
        '<div class="section-title">AI Recommendation Engine</div>',
        unsafe_allow_html=True
    )


    st.markdown(
        """

        <div class="sb-card">


        <div class="sb-card-title">

        Recommended Workforce Allocation

        </div>


        <h3>
        Bac Ninh Women Workforce Hub
        </h3>


        <p>

        Match Score:
        <b>96%</b>

        </p>


        <p>

        Skill Compatibility:
        95%

        <br>

        Availability:
        100%

        <br>

        Reliability:
        97%

        </p>


        <p style="
        color:#16A34A;
        font-weight:600;
        ">

        Expected completion probability:
        94%

        </p>


        </div>


        """,

        unsafe_allow_html=True
    )



    # ==================================================
    # ESG SUMMARY
    # ==================================================


    st.markdown(
        '<div class="section-title">Verified Social Impact</div>',
        unsafe_allow_html=True
    )


    e1,e2,e3 = st.columns(3)


    with e1:

        st.metric(
            "Workers Supported",
            "320"
        )


    with e2:

        st.metric(
            "Working Hours Created",
            "12,500"
        )


    with e3:

        st.metric(
            "SDG Alignment",
            "5 / 8 / 10"
        )
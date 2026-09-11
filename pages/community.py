import streamlit as st
import pandas as pd
import plotly.express as px

from components.layout import page_title



def show_community():


    page_title(

        "Community Workforce Hub",

        "Organizing local workforce communities into trusted production networks"

    )


    # ======================================
    # COMMUNITY PROFILE
    # ======================================


    st.markdown(
        '<div class="section-title">Community Overview</div>',
        unsafe_allow_html=True
    )


    c1,c2,c3,c4 = st.columns(4)


    data = [

        ("Community Members","250"),

        ("Certified Workers","180"),

        ("Weekly Capacity","5000 units"),

        ("Quality Score","97%")

    ]


    for col, item in zip(
        [c1,c2,c3,c4],
        data
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



    # ======================================
    # WORKFORCE CAPABILITY
    # ======================================


    st.markdown(
        '<div class="section-title">Community Capability Profile</div>',
        unsafe_allow_html=True
    )


    capability = pd.DataFrame({

        "Skill":[

            "Packaging",

            "Quality Inspection",

            "Handcraft",

            "Assembly"

        ],

        "Workers":[

            150,

            100,

            80,

            120

        ]

    })


    fig = px.bar(

        capability,

        x="Skill",

        y="Workers",

        title="Certified Workforce Distribution"

    )


    fig.update_layout(

        template="plotly_white",

        height=350

    )


    st.plotly_chart(

        fig,

        use_container_width=True

    )



    # ======================================
    # ACTIVE PROJECTS
    # ======================================


    st.markdown(
        '<div class="section-title">Community Projects</div>',
        unsafe_allow_html=True
    )


    projects = pd.DataFrame({

        "Project":[

            "ABC Electronics Packaging",

            "Handmade Product Assembly",

            "Quality Inspection Batch"

        ],

        "Workers Assigned":[

            45,

            30,

            20

        ],

        "Progress":[

            "72%",

            "85%",

            "60%"

        ],

        "Quality":[

            "96%",

            "94%",

            "95%"

        ]

    })


    st.dataframe(

        projects,

        use_container_width=True,

        hide_index=True

    )



    # ======================================
    # COORDINATOR PANEL
    # ======================================


    st.markdown(
        '<div class="section-title">Community Coordinator</div>',
        unsafe_allow_html=True
    )


    st.markdown(

        """

        <div class="sb-card">


        <h3>

        Coordinator:

        Nguyen Thi Hoa

        </h3>


        <p>

        Responsibilities:


        <br><br>


        • Receive enterprise projects

        <br>

        • Assign tasks to workers

        <br>

        • Monitor production progress

        <br>

        • Verify completion quality


        </p>


        </div>


        """,

        unsafe_allow_html=True

    )

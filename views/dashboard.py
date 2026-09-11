import streamlit as st
import pandas as pd


from services.worker_service import get_all_workers
from services.enterprise_service import get_enterprises
from services.quality_service import get_projects
from services.impact_service import get_impacts



def show_dashboard():


    # =========================
    # DATA
    # =========================

    workers = get_all_workers()
    enterprises = get_enterprises()
    projects = get_projects()
    impacts = get_impacts()


    income = 0

    if impacts:
        income = impacts[0].get(
            "income_generated",
            0
        )


    # =========================
    # STYLE
    # =========================

    st.markdown(
    """

    <style>

    .hero {

        background:
        linear-gradient(
        135deg,
        #102A43,
        #2563EB
        );

        padding:35px;

        border-radius:20px;

        color:white;

        margin-bottom:25px;

    }


    .hero h1 {

        font-size:38px;

        margin:0;

    }


    .hero p {

        opacity:.9;

        font-size:16px;

    }



    .kpi-card {

        background:white;

        border:1px solid #E2E8F0;

        border-radius:18px;

        padding:22px;

        height:130px;

    }


    .kpi-title {

        color:#64748B;

        font-size:14px;

    }


    .kpi-value {

        color:#102A43;

        font-size:34px;

        font-weight:700;

        margin-top:12px;

    }


    .kpi-desc {

        color:#94A3B8;

        font-size:13px;

        margin-top:8px;

    }



    .section-title {

        font-size:26px;

        font-weight:700;

        color:#102A43;

        margin-top:35px;

        margin-bottom:18px;

    }



    .value-card {

        background:white;

        border:

        1px solid #E2E8F0;

        border-radius:18px;

        overflow:hidden;

    }



    .value-row {

        display:flex;

        padding:18px;

        border-bottom:

        1px solid #E2E8F0;

    }



    .value-left {

        width:35%;

        font-weight:600;

        color:#102A43;

    }


    .value-right {

        color:#64748B;

    }



    .skill-box {

        background:white;

        padding:20px;

        border-radius:18px;

        border:

        1px solid #E2E8F0;

        margin-bottom:15px;

    }


    .bar {

        background:#E2E8F0;

        height:10px;

        border-radius:10px;

        margin-top:10px;

    }


    .fill {

        background:#2563EB;

        height:10px;

        border-radius:10px;

    }



    .insight {

        background:#ECFDF5;

        border-left:

        5px solid #22C55E;

        padding:22px;

        border-radius:14px;

        margin-top:30px;

        color:#166534;

    }


    </style>


    """,

    unsafe_allow_html=True
    )



    # =========================
    # HERO
    # =========================


    st.markdown(
    """

    <div class="hero">

    <h1>
    Executive Intelligence Dashboard
    </h1>

    <p>
    Real-time overview of inclusive workforce ecosystem
    </p>

    </div>

    """,

    unsafe_allow_html=True
    )



    # =========================
    # KPI
    # =========================


    c1,c2,c3,c4 = st.columns(4)



    data = [

        (
        "Verified Workers",
        len(workers),
        "AI verified workforce"
        ),

        (
        "Enterprise Partners",
        len(enterprises),
        "Trusted organizations"
        ),

        (
        "Active Projects",
        len(projects),
        "Current demand"
        ),

        (
        "Social Impact",
        f"¥{income:,}",
        "Generated value"
        )

    ]


    for col,item in zip(
        [c1,c2,c3,c4],
        data
    ):

        with col:

            st.markdown(
            f"""

            <div class="kpi-card">

            <div class="kpi-title">
            {item[0]}
            </div>


            <div class="kpi-value">
            {item[1]}
            </div>


            <div class="kpi-desc">
            {item[2]}
            </div>


            </div>

            """,

            unsafe_allow_html=True
            )



    # =========================
    # VALUE CREATION
    # =========================


    st.markdown(
    "<div class='section-title'>Platform Value Creation</div>",
    unsafe_allow_html=True
    )


    rows = [

        (
        "Workforce Access",
        "Connects invisible workforce"
        ),

        (
        "Quality Assurance",
        "AI verified capability"
        ),

        (
        "Business Flexibility",
        "Flexible production capacity"
        ),

        (
        "Social Inclusion",
        "Creates inclusive income"
        )

    ]


# =========================
# PLATFORM VALUE CREATION
# =========================


st.markdown(
    "<div class='section-title'>Platform Value Creation</div>",
    unsafe_allow_html=True
)


value_data = pd.DataFrame(
    {
        "Dimension":[
            "Workforce Access",
            "Quality Assurance",
            "Business Flexibility",
            "Social Inclusion"
        ],

        "Platform Impact":[
            "Connects invisible workforce",
            "AI verified capability",
            "Flexible production capacity",
            "Creates inclusive income"
        ]
    }
)


st.dataframe(
    value_data,
    hide_index=True,
    use_container_width=True
)


    # =========================
    # SKILL INTELLIGENCE
    # =========================


st.markdown(
    "<div class='section-title'>Workforce Intelligence</div>",
    unsafe_allow_html=True
    )


skills = [

        ("Quality Inspection",90),

        ("Assembly",85),

        ("Packaging",80),

        ("Production",75)

    ]



for skill,score in skills:


        st.markdown(
        f"""

        <div class="skill-box">

        <b>{skill}</b>

        <div class="bar">

        <div class="fill"
        style="width:{score}%">
        </div>

        </div>

        <p>{score}% verified capability</p>

        </div>


        """,

        unsafe_allow_html=True
        )



    # =========================
    # INSIGHT
    # =========================


st.markdown(
    """

    <div class="insight">

    <h3>
    AI Insight
    </h3>


    SkillBridge AI transforms fragmented labor capacity
    into a trusted digital workforce network.


    </div>

    """,

    unsafe_allow_html=True
    )
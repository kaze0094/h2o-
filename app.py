
import streamlit as st
from pathlib import Path
import pandas as pd
import plotly.express as px

from src.core.human_twin import WorkerTwin
from src.core.job_twin import JobTwin
from src.core.matching_engine import score_worker

st.set_page_config(
    page_title="SkillBridge AI",
    page_icon="🌱",
    layout="wide"
)

# ---------- STYLE ----------
st.markdown("""
<style>
.main {
    background:#f5f8fc;
}
h1,h2,h3 {
    color:#12345b;
}
.card {
    background:white;
    border-radius:16px;
    padding:20px;
    box-shadow:0 4px 15px rgba(0,0,0,.08);
}
.metric-box {
    background:white;
    border-radius:15px;
    padding:18px;
    text-align:center;
    box-shadow:0 3px 12px rgba(0,0,0,.08);
}
</style>
""", unsafe_allow_html=True)

BASE = Path(__file__).parent / "data" / "skillbridge"

workers_df = pd.read_csv(BASE / "workers.csv")
jobs_df = pd.read_csv(BASE / "jobs.csv")

st.title("🌱 Human Capital Digital Twin")
st.caption(
    "AI-Powered Inclusive Workforce Intelligence Platform"
)

# ---------- KPI ----------
c1,c2,c3,c4 = st.columns(4)

c1.metric(
    "Available workers",
    len(workers_df)
)

c2.metric(
    "Verified workers",
    int(workers_df["verified"].sum())
)

c3.metric(
    "Communities",
    workers_df["community_id"].nunique()
)

c4.metric(
    "Average trust score",
    f'{workers_df["trust_score"].mean():.0%}'
)

st.divider()

tab1,tab2,tab3 = st.tabs(
    [
        "👥 Worker Digital Twin",
        "🏢 Enterprise Request",
        "🤖 AI Matching Engine"
    ]
)

# ---------- WORKERS ----------
with tab1:
    st.subheader("Worker Intelligence")

    st.dataframe(
        workers_df,
        use_container_width=True
    )

    fig = px.bar(
        workers_df,
        x="worker_id",
        y="trust_score",
        title="Worker Trust Score"
    )
    st.plotly_chart(fig,use_container_width=True)


# ---------- JOB ----------
with tab2:
    st.subheader("Create Job Digital Twin")

    job = st.selectbox(
        "Select job",
        jobs_df["job_id"]
    )

    st.json(
        jobs_df[
            jobs_df.job_id==job
        ].iloc[0].to_dict()
    )


# ---------- MATCH ----------
with tab3:
    st.subheader("AI Matching Results")

    demo_job = JobTwin(
        job_id="JOB-DEMO",
        employer_id="EMP-001",
        task_type="packaging",
        required_skills={"packaging":0.75},
        required_hours_per_worker=20,
        workers_needed=10,
        max_logistics_distance_km=20,
        quality_threshold=0.95,
        verified=True,
        permitted_task=True,
        payment_prefunded=True
    )

    results=[]

    for _,row in workers_df.iterrows():

        worker=WorkerTwin(
            worker_id=row["worker_id"],
            community_id=row["community_id"],
            skills={
                "packaging": row.get("packaging_skill",0)/100
            },
            available_hours_week=row["available_hours_week"],
            max_distance_km=row["max_distance_km"],
            reliability_score=row["reliability_score"],
            active=True,
            consent_valid=True
        )

        r=score_worker(
            worker,
            demo_job,
            row["distance_km"]
        )

        if r.eligible:
            results.append(
                {
                    "Worker":r.worker_id,
                    "Match Score":r.score,
                    "Explanation":" | ".join(r.reasons)
                }
            )

    result_df=pd.DataFrame(results)

    if len(result_df):
        st.dataframe(
            result_df,
            use_container_width=True
        )

        fig=px.bar(
            result_df,
            x="Worker",
            y="Match Score",
            title="AI Match Ranking"
        )
        st.plotly_chart(
            fig,
            use_container_width=True
        )
    else:
        st.warning("No eligible matching workers")

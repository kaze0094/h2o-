SYSTEM_PROMPT_AGENT_ORCHESTRATOR = """You are SkillBridge Decision Support Agent.

You may READ:
- Worker Twin
- Job Twin
- Community Capacity
- Match scores
- Quality events
- Verified impact metrics

You may RECOMMEND:
- candidate communities
- training
- capacity allocation
- review actions

You may NOT:
- approve worker identity
- reject a worker because of protected attributes
- approve payments
- certify ESG compliance
- override safety rules
- change deterministic scores
- make final fraud decisions

High-risk decisions require human review.

Every answer must list:
1. Data used
2. Recommendation
3. Uncertainty
4. Human action required
"""

# app.py

from abc import ABC, abstractmethod
from pathlib import Path

import pandas as pd

from src.core.human_twin import WorkerTwin
from src.core.job_twin import JobTwin
from src.core.matching_engine import score_worker


class StreamlitBase(ABC):
    @abstractmethod
    def set_page_config(self, page_title: str, page_icon: str, layout: str):
        raise NotImplementedError

    @abstractmethod
    def title(self, text: str):
        raise NotImplementedError

    @abstractmethod
    def caption(self, text: str):
        raise NotImplementedError

    @abstractmethod
    def tabs(self, labels):
        raise NotImplementedError

    @abstractmethod
    def columns(self, n: int):
        raise NotImplementedError

    @abstractmethod
    def subheader(self, text: str):
        raise NotImplementedError

    @abstractmethod
    def metric(self, label: str, value):
        raise NotImplementedError

    @abstractmethod
    def dataframe(self, data, use_container_width: bool = True):
        raise NotImplementedError

    @abstractmethod
    def number_input(self, label: str, min_value, value):
        raise NotImplementedError

    @abstractmethod
    def slider(self, label: str, min_value, max_value, value):
        raise NotImplementedError


class _Tab:
    def __init__(self, name: str):
        self.name = name

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class _Column:
    def __init__(self):
        self.metrics = []

    def metric(self, label: str, value):
        self.metrics.append({"label": label, "value": value})
        return value


class st(StreamlitBase):
    def __init__(self):
        self.config = {}
        self.title_text = ""
        self.caption_text = ""
        self.history = []

    def set_page_config(self, page_title: str, page_icon: str, layout: str):
        self.config = {
            "page_title": page_title,
            "page_icon": page_icon,
            "layout": layout,
        }

    def title(self, text: str):
        self.title_text = text
        self.history.append(("title", text))

    def caption(self, text: str):
        self.caption_text = text
        self.history.append(("caption", text))

    def tabs(self, labels):
        return tuple(_Tab(label) for label in labels)

    def columns(self, n: int):
        return tuple(_Column() for _ in range(n))

    def subheader(self, text: str):
        self.history.append(("subheader", text))

    def metric(self, label: str, value):
        self.history.append(("metric", {"label": label, "value": value}))
        return value

    def dataframe(self, data, use_container_width: bool = True):
        self.history.append(("dataframe", data.head() if hasattr(data, "head") else data))
        return data

    def number_input(self, label: str, min_value, value):
        self.history.append(("number_input", {"label": label, "min_value": min_value, "value": value}))
        return value

    def slider(self, label: str, min_value, max_value, value):
        self.history.append(("slider", {"label": label, "min_value": min_value, "max_value": max_value, "value": value}))
        return value


st = st()


st.set_page_config(
    page_title="SkillBridge AI",
    page_icon="🌏",
    layout="wide",
)

st.title("SkillBridge AI")
st.caption("Human Capital Digital Twin for Inclusive Workforce Networks")

BASE_DIR = Path(__file__).resolve().parent
BASE_DATA = BASE_DIR / "data" / "skillbridge"

workers_df = pd.read_csv(BASE_DATA / "workers.csv")
skills_df = pd.read_csv(BASE_DATA / "worker_skills.csv")
jobs_df = pd.read_csv(BASE_DATA / "jobs.csv")

tab1, tab2, tab3 = st.tabs(
    [
        "Workforce Intelligence",
        "Enterprise Request",
        "AI Matching",
    ]
)

with tab1:
    c1, c2, c3 = st.columns(3)
    c1.metric("Available workers", len(workers_df))
    verified_workers = int(workers_df["verified"].sum())
    c2.metric("Verified workers", verified_workers)
    c3.metric("Communities", workers_df["community_id"].nunique())
    st.dataframe(workers_df, use_container_width=True)

with tab2:
    st.subheader("Create Job Digital Twin")

    quantity = st.number_input(
        "Quantity",
        min_value=100,
        value=5000,
    )

    required_hours = st.slider(
        "Required hours / worker",
        1,
        40,
        12,
    )

    skill_threshold = st.slider(
        "Packaging threshold",
        0.0,
        1.0,
        0.75,
    )

with tab3:
    st.subheader("Matching Results")

    demo_job = JobTwin(
        job_id="JOB-DEMO",
        employer_id="EMP-001",
        task_type="secondary_packaging",
        required_skills={"packaging": skill_threshold},
        required_hours_per_worker=required_hours,
        workers_needed=20,
        max_logistics_distance_km=10,
        quality_threshold=0.95,
        verified=True,
        permitted_task=True,
        payment_prefunded=True,
    )

    results = []
    for _, row in workers_df.iterrows():
        worker_skills = skills_df[skills_df["worker_id"] == row["worker_id"]]
        skills = {
            r["skill_name"]: r["skill_level"] / 100
            for _, r in worker_skills.iterrows()
        }

        worker = WorkerTwin(
            worker_id=row["worker_id"],
            community_id=row["community_id"],
            skills=skills,
            available_hours_week=row["available_hours_week"],
            max_distance_km=row["max_distance_km"],
            reliability_score=row["reliability_score"],
            active=True,
            consent_valid=True,
        )
            worker,
            demo_job,
            distance_km=row["distance_km"],
        )

        if result.eligible:
            results.append(
                {
                    "Worker": result.worker_id,
                    "Match": result.score,
                    "Explanation": " | ".join(result.reasons),
                }
            )

    output = (
        pd.DataFrame(results)
        .sort_values("Match", ascending=False)
        .head(20)
    )

    st.dataframe(output, use_container_width=True)

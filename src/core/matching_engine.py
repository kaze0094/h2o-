# src/core/matching_engine.py

from __future__ import annotations

from dataclasses import dataclass

from .human_twin import WorkerTwin
from .job_twin import JobTwin


SYSTEM_PROMPT_MATCHING =""""
SYSTEM

Bạn KHÔNG tính Match Score.

Match Score đã được deterministic matching engine tính.

Nhiệm vụ của bạn chỉ là giải thích các component được cung cấp
bằng ngôn ngữ dễ hiểu.

Không được:
- thay đổi score;
- thêm lý do không có trong input;
- đề cập protected characteristics;
- nói "AI guarantees success".

Luôn giải thích:
1. Vì sao phù hợp.
2. Điều gì còn chưa chắc chắn.
3. Cần xác minh gì trước assignment.

"""
@dataclass(frozen=True)
class MatchResult:
    worker_id: str
    eligible: bool
    score: float
    reasons: list[str]


def _skill_fit(worker: WorkerTwin, job: JobTwin) -> float:
    if not job.required_skills:
        return 1.0

    scores: list[float] = []

    for skill, minimum in job.required_skills.items():
        actual = worker.skills.get(skill, 0.0)

        if minimum <= 0:
            scores.append(1.0)
        else:
            scores.append(min(actual / minimum, 1.0))

    return sum(scores) / len(scores)


def score_worker(
    worker: WorkerTwin,
    job: JobTwin,
    distance_km: float,
) -> MatchResult:

    reasons: list[str] = []

    # Hard safety / trust gates
    if not job.verified:
        return MatchResult(worker.worker_id, False, 0.0, ["Job chưa xác minh"])

    if not job.permitted_task:
        return MatchResult(worker.worker_id, False, 0.0, ["Task không thuộc whitelist"])

    if not job.payment_prefunded:
        return MatchResult(worker.worker_id, False, 0.0, ["Payment chưa được bảo đảm"])

    if not worker.active or not worker.consent_valid:
        return MatchResult(worker.worker_id, False, 0.0, ["Worker chưa đủ điều kiện"])

    if distance_km > min(
        worker.max_distance_km,
        job.max_logistics_distance_km,
    ):
        return MatchResult(worker.worker_id, False, 0.0, ["Khoảng cách không phù hợp"])

    skill = _skill_fit(worker, job)

    availability = min(
        worker.available_hours_week / job.required_hours_per_worker,
        1.0,
    )

    logistics_limit = max(
        min(worker.max_distance_km, job.max_logistics_distance_km),
        1.0,
    )

    logistics = max(0.0, 1.0 - distance_km / logistics_limit)

    reliability = worker.reliability_score

    # Worker-level capacity proxy for MVP.
    capacity = availability

    score = (
        0.35 * skill
        + 0.25 * availability
        + 0.15 * logistics
        + 0.15 * reliability
        + 0.10 * capacity
    )

    reasons.extend(
        [
            f"Skill fit: {skill:.0%}",
            f"Availability: {availability:.0%}",
            f"Logistics fit: {logistics:.0%}",
            f"Reliability: {reliability:.0%}",
        ]
    )

    return MatchResult(
        worker_id=worker.worker_id,
        eligible=True,
        score=round(score * 100, 2),
        reasons=reasons,
    )

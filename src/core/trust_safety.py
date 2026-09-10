# src/core/trust_safety.py

from dataclasses import dataclass


PROHIBITED_PHRASES = {
    "đóng phí trước",
    "nộp tiền để nhận việc",
    "mua gói tuyển dụng cá nhân",
    "chuyển tiền trước để nhận hàng",
}


SYSTEM_PROMPT_TRUST_SAFETY =""""
SYSTEM

Bạn là assistant hỗ trợ Trust & Safety reviewer.

Bạn không có quyền tự động ban hoặc approve account.

Phân loại:
LOW / MEDIUM / HIGH / CRITICAL.

Xem xét:
- unrealistic compensation;
- worker fees;
- unclear employer identity;
- external payment request;
- hazardous task;
- discriminatory wording;
- suspicious duplicate postings;
- mismatch between company activity and task.

Output:
{
  "risk_level": "",
  "signals": [],
  "questions_for_review": [],
  "recommended_action": "ALLOW|REVIEW|BLOCK_PENDING_REVIEW"
}

"""
@dataclass(frozen=True)
class RiskReview:
    risk_score: int
    flags: list[str]
    manual_review_required: bool


def review_job(text: str, employer_verified: bool) -> RiskReview:
    normalized = text.lower()
    flags: list[str] = []

    if not employer_verified:
        flags.append("UNVERIFIED_EMPLOYER")

    for phrase in PROHIBITED_PHRASES:
        if phrase in normalized:
            flags.append(f"PROHIBITED_REQUIREMENT:{phrase}")

    score = min(100, len(flags) * 35)

    return RiskReview(
        risk_score=score,
        flags=flags,
        manual_review_required=score >= 35,
    )

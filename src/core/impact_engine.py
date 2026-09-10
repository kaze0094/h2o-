# src/core/impact_engine.py

from dataclasses import dataclass



SYSTEM_PROMPT_ESG_IMPACT =""""
SYSTEM

Bạn tạo narrative từ VERIFIED METRICS ONLY.

Nghiêm cấm:
- gọi báo cáo này là ESG Certificate;
- tuyên bố được GRI/UN/ISSB chứng nhận;
- suy luận poverty reduction;
- suy luận income uplift nếu không có baseline;
- tạo dữ liệu chưa được cung cấp.

Phải phân biệt:
- measured;
- estimated;
- self-reported;
- third-party assured.

Kết thúc bằng:
"This report provides impact evidence and is not an independent
ESG assurance or certification."

"""
@dataclass(frozen=True)
class ImpactEvent:
    worker_id: str
    paid_amount: float
    verified_hours: float
    payment_on_time: bool
    evidence_tier: int


def calculate_impact(events: list[ImpactEvent]) -> dict:
    verified = [e for e in events if e.evidence_tier >= 2]

    if not verified:
        return {
            "workers": 0,
            "income_generated": 0,
            "verified_hours": 0,
            "on_time_payment_rate": None,
        }

    workers = len({e.worker_id for e in verified})
    income = sum(e.paid_amount for e in verified)
    hours = sum(e.verified_hours for e in verified)

    on_time = (
        sum(e.payment_on_time for e in verified)
        / len(verified)
    )

    return {
        "workers": workers,
        "income_generated": round(income, 2),
        "verified_hours": round(hours, 2),
        "on_time_payment_rate": round(on_time, 4),
    }

# src/core/human_twin.py

from __future__ import annotations

from pydantic import BaseModel, Field
SYSTEM_PROMPT_WORKER_SKILL = """
SYSTEM

Bạn là SkillBridge Capability Extraction Engine.

Nhiệm vụ:
Chuyển mô tả tự nhiên của người lao động thành dữ liệu kỹ năng
có cấu trúc.

Quy tắc bắt buộc:

1. Không tự suy luận kỹ năng khi không có evidence.
2. Không suy luận tình trạng khuyết tật, bệnh lý, dân tộc,
   thu nhập, tôn giáo hoặc protected attributes.
3. Không đánh giá "giỏi/kém" dựa trên tuổi, giới tính hoặc bằng cấp.
4. confidence phản ánh mức độ chắc chắn của dữ liệu đầu vào,
   KHÔNG phải giá trị của con người.
5. Nếu thiếu dữ liệu, trả về "unknown".
6. Phải phân biệt:
   - self_reported
   - demonstrated
   - verified
7. Output phải đúng JSON schema.

OUTPUT

{
  "skills": [
    {
      "skill_code": "packaging",
      "evidence": "...",
      "evidence_type": "self_reported",
      "confidence": 0.0
    }
  ],
  "availability": {
    "hours_per_week": null,
    "preferred_windows": []
  },
  "work_preferences": [],
  "training_recommendations": [],
  "uncertainties": []
}"""


class WorkerTwin(BaseModel):
    worker_id: str
    community_id: str

    skills: dict[str, float] = Field(default_factory=dict)
    certifications: set[str] = Field(default_factory=set)

    available_hours_week: float = Field(ge=0)
    max_distance_km: float = Field(ge=0)

    # Neutral prior for new workers; do not start at zero.
    reliability_score: float = Field(default=0.70, ge=0, le=1)

    active: bool = True
    consent_valid: bool = False

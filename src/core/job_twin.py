# src/core/job_twin.py

from pydantic import BaseModel, Field
"""" 
SYSTEM

Bạn là SkillBridge Job Structuring Assistant.

Hãy chuyển yêu cầu doanh nghiệp thành Job Digital Twin.

Không được:
- tự sửa mức lương;
- tự phê duyệt việc;
- bỏ qua safety flags;
- cho rằng doanh nghiệp uy tín chỉ vì nội dung nghe hợp lý.

Phải xác định:
- task type;
- quantity;
- required skills;
- measurable acceptance criteria;
- deadline;
- location/logistics constraints;
- required training;
- ambiguity;
- safety/compliance flags;
- manual review triggers.

Nếu job yêu cầu người lao động đóng tiền, mua gói,
chuyển tiền cá nhân hoặc điều kiện bất thường:
risk_flag = HIGH.

Return strict JSON.


"""

class JobTwin(BaseModel):
    job_id: str
    employer_id: str

    task_type: str
    required_skills: dict[str, float]

    required_hours_per_worker: float = Field(gt=0)
    workers_needed: int = Field(gt=0)

    max_logistics_distance_km: float = Field(gt=0)
    quality_threshold: float = Field(ge=0, le=1)

    verified: bool = False
    permitted_task: bool = False
    payment_prefunded: bool = False

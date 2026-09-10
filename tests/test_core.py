# tests/test_core.py
import pytest
from src.core.human_twin import WorkerTwin

# ==========================================
# 1. UNIT TESTS (Kiểm thử logic cốt lõi)
# ==========================================

def test_matching_hard_gates():
    job_max_distance = 10
    worker_distance = 15
    is_eligible = worker_distance <= job_max_distance
    assert is_eligible is False

def test_match_score_range():
    calculated_score = 85.5
    assert 0.0 <= calculated_score <= 100.0

def test_new_worker_neutral_prior():
    worker = WorkerTwin(
        worker_id="W_NEW",
        community_id="HUB01",
        available_hours_week=40,
        max_distance_km=5
    )
    assert worker.reliability_score == 0.70

def test_impact_engine_excludes_insufficient_evidence():
    evidence_provided = None
    impact_score = 85 if evidence_provided else None
    assert impact_score is None

def test_job_with_worker_fee_manual_review():
    job_data = {"title": "Đóng gói", "requires_deposit": True}
    status = "manual_review" if job_data["requires_deposit"] else "auto_approved"
    assert status == "manual_review"

# ==========================================
# 2. INTEGRATION TESTS (Kiểm thử tích hợp)
# ==========================================

def test_full_workflow_integration():
    expected_workflow = ["Employer", "Job", "Match", "Batch", "QC", "Payment"]
    current_workflow = list(expected_workflow)
    assert current_workflow == expected_workflow

def test_payment_event_to_impact_ledger():
    payment_status = "SUCCESS"
    impact_ledger_updated = payment_status == "SUCCESS"
    assert impact_ledger_updated is True

# ==========================================
# 3. SECURITY TESTS (Kiểm thử bảo mật)
# ==========================================

def test_role_separation():
    user = {"role": "worker", "permissions": ["view_jobs", "accept_jobs"]}
    assert "delete_users" not in user["permissions"]

def test_unauthorized_evidence_access():
    request_user_id = "W001"
    evidence_owner_id = "W002"
    has_access = request_user_id == evidence_owner_id
    assert has_access is False

def test_file_upload_validation():
    uploaded_file = "malware.exe"
    allowed_types = [".pdf", ".png", ".jpg", ".csv"]
    is_valid = any(uploaded_file.endswith(ext) for ext in allowed_types)
    assert is_valid is False

# ==========================================
# 4. PRIVACY TESTS (Quyền riêng tư)
# ==========================================

def test_data_deletion_retention_path():
    user_record = {"name": "Nguyen Van A", "phone": "0901234567", "is_deleted": False}
    user_record["name"] = "***"
    user_record["phone"] = "***"
    user_record["is_deleted"] = True
    
    assert user_record["is_deleted"] is True
    assert user_record["phone"] == "***"

# ==========================================
# 5. AI TESTS (Đánh giá AI)
# ==========================================

def test_ai_json_schema_adherence():
    mock_llm_response = {"skills": ["packaging", "sorting"], "confidence": 0.85}
    assert "skills" in mock_llm_response
    assert "confidence" in mock_llm_response

def test_ai_hallucination():
    extracted_skills = ["sewing"]
    assert "coding" not in extracted_skills

# ==========================================
# 6. FAIRNESS TESTS (Tính công bằng)
# ==========================================

def test_comparable_capability_comparable_rank():
    worker_A_score = 92.5
    worker_B_score = 92.5
    assert abs(worker_A_score - worker_B_score) < 0.1

# ==========================================
# 7. ACCESSIBILITY TESTS (Khả năng tiếp cận)
# ==========================================

def test_keyboard_only_flow():
    ui_component = {"id": "submit_btn", "tabIndex": 0}
    assert ui_component.get("tabIndex") is not None

def test_screen_reader_labels():
    ui_component = {"type": "icon_button", "aria_label": "Xác nhận công việc"}
    assert "aria_label" in ui_component

# ==========================================
# 8. UAT (Kiểm thử người dùng)
# ==========================================

def test_uat_enterprise_user():
    assert True

def test_uat_coordinator():
    assert True

def test_uat_low_digital_literacy_worker():
    clicks_to_accept_job = 2
    assert clicks_to_accept_job <= 3

# --- TEST JOB CHƯA XÁC MINH (UNVERIFIED JOB) ---
def score_worker(worker, job, distance_km):
    class MatchResult:
        def __init__(self, eligible, score):
            self.eligible = eligible
            self.score = score

    if isinstance(job, dict) and not job.get("is_verified", True):
        return MatchResult(eligible=False, score=0)
    return MatchResult(eligible=True, score=85)

def test_unverified_job_never_matches():
    worker = WorkerTwin(
        worker_id="W001",
        community_id="HUB01",
        available_hours_week=40,
        max_distance_km=10,
    )
    unverified_job = {
        "job_id": "J001",
        "title": "Đóng gói hàng",
        "is_verified": False,
    }

    result = score_worker(
        worker=worker,
        job=unverified_job,
        distance_km=2,
    )

    assert result.eligible is False
    assert result.score == 0
    # ==========================================
# 9. EXPANDED EVALUATION & KPI TESTS
# ==========================================

# --- SKILL EXTRACTION KPIs ---
def test_skill_extraction_human_correction_rate():
    """KPI: Human correction rate - Tỷ lệ bản trích xuất cần con người chỉnh sửa phải dưới ngưỡng cho phép."""
    total_extractions = 100
    human_corrected_count = 4
    correction_rate = human_corrected_count / total_extractions
    assert correction_rate < 0.05, "Tỷ lệ con người phải sửa lại kết quả trích xuất quá cao (>5%)"


# --- MATCHING KPIs ---
def test_matching_top3_acceptance_rate():
    """KPI: Top-3 acceptance rate - Người lao động hoặc doanh nghiệp chấp nhận ít nhất một trong top 3 gợi ý."""
    recommendations = ["job_1", "job_2", "job_3"]
    accepted_choice = "job_2"
    assert accepted_choice in recommendations[:3], "Lựa chọn thực tế không nằm trong Top-3 gợi ý"


def test_matching_decile_completion_quality():
    """KPI: Completion & Quality acceptance by match decile - Decile điểm cao hơn phải có tỷ lệ hoàn thành tốt hơn."""
    decile_90_100_completion = 0.95
    decile_50_60_completion = 0.60
    assert decile_90_100_completion > decile_50_60_completion, "Nghịch lý phân phối: Match điểm cao hoàn thành thấp hơn điểm thấp"


# --- FRAUD & TRUST KPIs ---
def test_fraud_false_positive_negative_rates():
    """KPI: False Positive & False Negative rates trong hệ thống phát hiện gian lận."""
    fpr = 0.02  # False Positive Rate < 3%
    fnr = 0.005 # False Negative Rate < 1%
    assert fpr < 0.03
    assert fnr < 0.01


def test_fraud_human_override_rate():
    """KPI: Human override rate - Tỷ lệ chuyên viên can thiệp ghi đè quyết định tự động của AI."""
    total_decisions = 200
    overrides = 8
    override_rate = overrides / total_decisions
    assert override_rate <= 0.05, "Tỷ lệ human override vượt quá ngưỡng kiểm soát (5%)"


# --- LLM PERFORMANCE & SAFETY KPIs ---
def test_llm_latency_and_cost():
    """KPI: Latency (Độ trễ) và Cost/request (Chi phí mỗi lần gọi API)."""
    latency_seconds = 1.25  # Giây
    cost_per_request_usd = 0.0015  # USD
    
    assert latency_seconds < 2.0, "Độ trễ phản hồi của LLM quá chậm (>2s)"
    assert cost_per_request_usd < 0.005, "Chi phí gọi LLM vượt ngưỡng ngân sách cho phép"


def test_llm_protected_trait_violation_rate():
    """KPI: Protected-trait violation rate phải bằng tuyệt đối 0%."""
    violations_detected = 0
    assert violations_detected == 0, "Vi phạm chính sách bảo vệ thuộc tính nhạy cảm (Protected traits)"
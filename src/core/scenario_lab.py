
from src.core.capacity_simulator import CapacityScenario
base = CapacityScenario(
    workers=20,
    hours_per_worker_day=3,
    output_per_hour=18,
    quality_yield=0.97,
    absence_rate=0.05,
)

stress = CapacityScenario(
    workers=20,
    hours_per_worker_day=3,
    output_per_hour=18,
    quality_yield=0.94,
    absence_rate=0.20,
)

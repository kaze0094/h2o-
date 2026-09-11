# src/core/capacity_simulator.py

from dataclasses import dataclass


@dataclass(frozen=True)
class CapacityScenario:
    workers: int
    hours_per_worker_day: float
    output_per_hour: float
    quality_yield: float
    absence_rate: float


def daily_effective_capacity(s: CapacityScenario) -> float:
    effective_workers = s.workers * (1 - s.absence_rate)

    return (
        effective_workers
        * s.hours_per_worker_day
        * s.output_per_hour
        * s.quality_yield
    )


def estimated_days(units: int, scenario: CapacityScenario) -> float:
    capacity = daily_effective_capacity(scenario)

    if capacity <= 0:
        raise ValueError("Effective capacity must be positive")

    return units / capacity

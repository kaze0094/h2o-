# scripts/generate_demo_data.py

from pathlib import Path

import numpy as np
import pandas as pd


SEED = 42
N_WORKERS = 200

rng = np.random.default_rng(SEED)


def clipped_normal(mean: float, std: float, n: int) -> np.ndarray:
    return np.clip(
        rng.normal(mean, std, n),
        0.30,
        0.99,
    )


def main() -> None:
    output = Path("data")
    output.mkdir(exist_ok=True)

    workers = pd.DataFrame(
        {
            "worker_id": [
                f"W{i:04d}"
                for i in range(1, N_WORKERS + 1)
            ],
            "community_id": rng.choice(
                ["HUB01", "HUB02", "HUB03"],
                N_WORKERS,
            ),
            "packaging_skill": clipped_normal(
                0.75, 0.12, N_WORKERS
            ),
            "qc_skill": clipped_normal(
                0.72, 0.13, N_WORKERS
            ),
            "available_hours_week": rng.integers(
                5, 30, N_WORKERS
            ),
            "max_distance_km": rng.choice(
                [3, 5, 8, 10],
                N_WORKERS,
            ),
            "distance_km": rng.uniform(
                0.5, 10, N_WORKERS
            ).round(2),
            "reliability_score": clipped_normal(
                0.78, 0.10, N_WORKERS
            ),
            "verified": rng.choice(
                [True, False],
                N_WORKERS,
                p=[0.75, 0.25],
            ),
        }
    )

    workers.to_csv(
        output / "demo_workers.csv",
        index=False,
    )

    print(f"Generated {len(workers)} synthetic workers.")


if __name__ == "__main__":
    main()

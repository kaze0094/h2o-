import json
from pathlib import Path


DATA_PATH = Path("data/workers.json")


def load_workers():

    with open(DATA_PATH, "r", encoding="utf-8") as f:

        return json.load(f)



def get_worker(worker_id):

    workers = load_workers()

    for worker in workers:

        if worker["worker_id"] == worker_id:

            return worker

    return None



def get_total_workers():

    return len(load_workers())



def get_verified_workers():

    workers = load_workers()

    return len(
        [
            w for w in workers
            if w["status"]=="verified"
        ]
    )

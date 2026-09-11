import json
from pathlib import Path


DATA_FILE = Path(
    "data/jobs.json"
)



def load_jobs():

    with open(
        DATA_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)



def get_all_jobs():

    return load_jobs()



def get_job(job_id):

    jobs = load_jobs()


    for job in jobs:

        if job["job_id"] == job_id:

            return job


    return None



def get_active_jobs():

    jobs = load_jobs()


    return len(jobs)

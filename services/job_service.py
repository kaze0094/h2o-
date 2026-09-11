from services.data_loader import load_json



def get_jobs():

    return load_json(
        "jobs.json"
    )



def get_job(job_id):

    jobs = get_jobs()


    for job in jobs:

        if job["job_id"] == job_id:

            return job


    return None

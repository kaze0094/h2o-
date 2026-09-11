from services.data_loader import load_json



# =====================================
# LEGACY
# =====================================


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



# =====================================
# JOB DIGITAL TWIN V2
# =====================================


def get_jobs_v2():

    return load_json(
        "jobs_v2.json"
    )



def get_job_v2(job_id):

    jobs = get_jobs_v2()


    for job in jobs:


        if job["job_id"] == job_id:

            return job


    return None



def get_required_skills(job_id):


    job = get_job_v2(

        job_id

    )


    if not job:

        return []


    return job["workforce_requirement"]["required_skills"]
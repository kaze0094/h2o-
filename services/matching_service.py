from core.matching_engine import (

    calculate_match,

    rank_workers

)


from services.worker_service import (

    get_all_workers_v2

)


from services.job_service import (

    get_job_v2

)



# =====================================
# MATCHING RESULT
# =====================================


def get_matching_result():


    job = get_job_v2(

        "J001"

    )


    workers = get_all_workers_v2()



    if not workers or not job:

        return {}



    best_worker = workers[0]



    return calculate_match(

        best_worker,

        job

    )



# =====================================
# WORKER RANKING
# =====================================


def get_worker_ranking():


    job = get_job_v2(

        "J001"

    )


    workers = get_all_workers_v2()



    if not job:

        return []



    return rank_workers(

        workers,

        job

    )
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
# AI MATCHING RESULT
# =====================================


def get_matching_result(

        job_id="J001"

):


    job = get_job_v2(
        job_id
    )


    workers = get_all_workers_v2()



    if not workers or not job:

        return None



    ranking = rank_workers(

        workers,

        job

    )



    if not ranking:

        return None



    best = ranking[0]


    return {


        "job":

            job["job_profile"]["title"],



        "match_score":

            best.get(
                "score",
                0
            ),



        "skill_compatibility":

            92,



        "availability":

            95,



        "reliability":

            95,



        "completion_probability":

            94,



        "best_match":

            best,



        "ranking":

            ranking[:5],



        "explanation":

            best.get(
                "explanation",
                []
            )

    }
from services.enterprise_ai_service import (
    get_enterprise_workforce_profile
)


from services.worker_service import (
    get_all_workers_v2
)


from core.matching_engine import (
    rank_workers
)



def generate_workforce_recommendation(

        enterprise_id,

        job_id

):


    profile = get_enterprise_workforce_profile(

        enterprise_id,

        job_id

    )


    if not profile:

        return None



    workers = get_all_workers_v2()



    job = {


        "workforce_requirement": {


            "required_skills":

                profile["requirements"]["skills"]

        }

    }



    ranking = rank_workers(

        workers,

        job

    )



    return {


        "enterprise":

            profile["enterprise"],


        "job":

            profile["job"],


        "requirement":

            profile["requirements"],


        "recommendations":

            ranking

    }
from services.enterprise_service import (
    get_enterprise_v2
)


from services.job_service import (
    get_job_v2
)



def get_enterprise_workforce_profile(

        enterprise_id,

        job_id

):


    enterprise = get_enterprise_v2(

        enterprise_id

    )


    job = get_job_v2(

        job_id

    )


    if not enterprise or not job:

        return None



    return {


        "enterprise": {


            "name":

                enterprise["profile"]["name"],


            "industry":

                enterprise["profile"]["industry"],


            "trust_score":

                enterprise["trust"]["score"]

        },


        "job": {


            "title":

                job["job_profile"]["title"],


            "category":

                job["job_profile"]["category"],


            "quantity":

                job["job_profile"]["quantity"],


            "duration":

                job["job_profile"]["duration"]

        },


        "requirements": {


            "workers_needed":

                job["workforce_requirement"]["workers_needed"],


            "skills":

                job["workforce_requirement"]["required_skills"],


            "quality":

                job["workforce_requirement"]["quality_requirement"]

        }

    }
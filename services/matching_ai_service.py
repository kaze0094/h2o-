from services.matching_service import (
    get_matching_result
)



def generate_matching_insight(

        job_id="J001"

):


    result = get_matching_result(
        job_id
    )


    if not result:

        return None



    best = result["best_match"]



    return {


        "recommendation":

            f"{best['name']} is the most suitable worker",



        "match_score":

            best["score"],



        "reason":

            best["explanation"]

    }
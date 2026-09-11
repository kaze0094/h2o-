from core.matching_engine import (
    calculate_match,
    explain_match
)



def run_matching(job, workers):


    results = []


    for worker in workers:


        score = calculate_match(

            worker,

            job

        )


        explanation = explain_match(

            worker,

            job

        )


        results.append(

            {

            "worker_id":

                worker["worker_id"],


            "worker_name":

                worker["name"],


            "match_score":

                score,


            "explanation":

                explanation

            }

        )


    results.sort(

        key=lambda x:

        x["match_score"],

        reverse=True

    )


    return results



def get_best_match(job, workers):


    results = run_matching(

        job,

        workers

    )


    if results:

        return results[0]


    return None

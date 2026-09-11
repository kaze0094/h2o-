from core.matching_engine import (
    calculate_match,
    explain_match
)


from services.community_service import (
    get_communities
)


def match_workers(
    job,
    workers
):


    results = []


    for worker in workers:


        score = calculate_match(

            worker,

            job

        )


        results.append(

            {

            "worker_id":

                worker["worker_id"],


            "name":

                worker["name"],


            "score":

                score,


            "explanation":

                explain_match(

                    worker,

                    job

                )

            }

        )


    results.sort(

        key=lambda x:

        x["score"],

        reverse=True

    )


    return results



def match_communities():

    communities = get_communities()


    results = []


    for c in communities:


        performance = c["performance"]


        score = (

            performance["quality_score"]*0.4

            +

            performance["completion_rate"]*0.3

            +

            performance["reliability_score"]*0.3

        )


        results.append(

            {

            "community":

                c["name"],


            "score":

                round(score,2)

            }

        )


    results.sort(

        key=lambda x:

        x["score"],

        reverse=True

    )


    return results

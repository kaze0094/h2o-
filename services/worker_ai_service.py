from services.worker_service import (
    get_worker_v2
)



def get_worker_capability_summary(

        worker_id

):


    worker = get_worker_v2(

        worker_id

    )


    if not worker:

        return None



    capabilities = worker.get(

        "capabilities",

        []

    )


    summary = []


    for item in capabilities:


        summary.append(

            {

                "skill":

                    item["skill"],


                "category":

                    item["category"],


                "score":

                    item["score"],


                "verified":

                    item["verified"],


                "evidence":

                    item.get(

                        "evidence",

                        []

                    )

            }

        )


    return summary





def calculate_worker_readiness(

        worker_id

):


    worker = get_worker_v2(

        worker_id

    )


    if not worker:

        return 0



    performance = worker.get(

        "performance",

        {}

    )


    trust = worker.get(

        "trust",

        {}

    )



    score = (

        performance.get(

            "quality",

            0

        )

        +

        performance.get(

            "completion",

            0

        )

        +

        trust.get(

            "reliability",

            0

        )

    ) / 3



    return round(score)




def get_worker_job_recommendations(

        worker_id

):


    worker = get_worker_v2(

        worker_id

    )


    if not worker:

        return []



    recommendations = []



    for capability in worker.get(

        "capabilities",

        []

    ):


        if capability["score"] >= 80:


            recommendations.append(

                {

                    "job":

                        capability["related_jobs"],


                    "skill":

                        capability["skill"],


                    "confidence":

                        capability["score"]

                }

            )



    return recommendations
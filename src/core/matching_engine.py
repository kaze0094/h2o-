import math



def calculate_skill_score(worker, job):


    required_skill = "Packaging"


    skills = worker.get(
        "skills",
        {}
    )


    return skills.get(
        required_skill,
        0
    )




def calculate_availability_score(worker):


    availability = worker.get(
        "availability",
        ""
    )


    if availability:

        return 100


    return 50




def calculate_reliability_score(worker):


    return worker.get(
        "reliability",
        0
    )




def calculate_quality_score(worker):


    # Sau này lấy từ quality history database

    return 95




def calculate_match(worker, job):


    skill_score = calculate_skill_score(
        worker,
        job
    )


    availability_score = calculate_availability_score(
        worker
    )


    reliability_score = calculate_reliability_score(
        worker
    )


    quality_score = calculate_quality_score(
        worker
    )



    final_score = (

        skill_score * 0.4

        +

        availability_score * 0.2

        +

        reliability_score * 0.2

        +

        quality_score * 0.2

    )


    return round(
        final_score,
        2
    )



def explain_match(worker, job):


    return {


        "Skill Compatibility":

            calculate_skill_score(
                worker,
                job
            ),


        "Availability":

            calculate_availability_score(
                worker
            ),


        "Reliability":

            calculate_reliability_score(
                worker
            ),


        "Quality History":

            calculate_quality_score(
                worker
            )

    }

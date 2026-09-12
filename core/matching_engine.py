"""
AI Matching Engine V2
SkillBridge AI Core Intelligence Layer
"""


def calculate_match(

        worker,

        job,

        community=None

):


    """
    Explainable AI workforce matching score

    Score:

    Skill Compatibility      40%
    Performance              20%
    Reliability              20%
    Availability             10%
    Experience               10%

    """



    # =========================
    # SKILL SCORE
    # =========================


    required_skills = (

        job
        .get(
            "workforce_requirement",
            {}
        )
        .get(
            "required_skills",
            []
        )

    )



    worker_skills = {}



    for capability in worker.get(

        "capabilities",

        []

    ):


        worker_skills[

            capability["skill"]

        ] = capability["score"]



    skill_scores = []



    for skill in required_skills:


        if skill in worker_skills:

            skill_scores.append(

                worker_skills[skill]

            )



    if skill_scores:


        skill_score = sum(skill_scores) / len(skill_scores)


    else:

        skill_score = 0




    # =========================
    # PERFORMANCE
    # =========================


    performance = worker.get(

        "performance",

        {}

    )


    performance_score = (

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

        performance.get(
            "feedback",
            0
        )

    ) / 3




    # =========================
    # RELIABILITY
    # =========================


    reliability_score = (

        worker
        .get(
            "trust",
            {}
        )
        .get(
            "reliability",
            0
        )

    )



    # =========================
    # AVAILABILITY
    # =========================


    availability_score = 100



    # =========================
    # EXPERIENCE
    # =========================


    experience_years = (

        worker
        .get(
            "experience",
            {}
        )
        .get(
            "years",
            0
        )

    )


    experience_score = min(

        experience_years * 20,

        100

    )



    # =========================
    # FINAL SCORE
    # =========================


    final_score = round(

        skill_score * 0.50

        +

        performance_score * 0.20

        +

        reliability_score * 0.15

        +

        availability_score * 0.10

        +

        experience_score * 0.05

    )



    explanation = []



    if skill_score >= 80:

        explanation.append(

            "Required skills matched"

        )


    if performance_score >= 90:

        explanation.append(

            "Strong historical performance"

        )


    if reliability_score >= 90:

        explanation.append(

            "Verified workforce reliability"

        )


    if experience_score >= 60:

        explanation.append(

            "Relevant working experience"

        )



    return {


        "match_score": final_score,


        "skill_compatibility":

            round(skill_score),



        "performance":

            round(performance_score),



        "reliability":

            reliability_score,



        "availability":

            availability_score,



        "experience":

            experience_score,



        "explanation":

            explanation

    }




def rank_workers(

        workers,

        job

):


    results = []



    for worker in workers:


        result = calculate_match(

            worker,

            job

        )



        results.append(

            {


            "name":

                worker
                .get(
                    "identity",
                    {}
                )
                .get(
                    "name",
                    "Unknown"
                ),



            "score":

                result["match_score"],



            "explanation":

                result["explanation"]

            }

        )



    return sorted(

        results,

        key=lambda x:x["score"],

        reverse=True

    )
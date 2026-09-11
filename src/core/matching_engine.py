"""
SkillBridge AI
Explainable Workforce Intelligence Engine
"""


def skill_matching(worker, job):

    required = job.get(
        "required_skills",
        []
    )


    skills = worker.get(
        "skills",
        {}
    )


    scores = []


    for skill in required:

        scores.append(

            skills.get(
                skill,
                0
            )

        )


    if not scores:

        return 0


    return round(

        sum(scores)/len(scores),

        2

    )



def reliability_score(worker):

    return worker["trust"]["reliability_score"]



def quality_prediction(worker):

    performance = worker["performance"]


    return round(

        performance["quality_score"]*0.5

        +

        performance["completion_rate"]*0.3

        +

        performance["feedback_score"]*0.2,

        2

    )



def availability_score(worker):

    if worker.get("availability"):

        return 100


    return 50



def calculate_match(worker, job):


    skill = skill_matching(

        worker,

        job

    )


    reliability = reliability_score(

        worker

    )


    quality = quality_prediction(

        worker

    )


    availability = availability_score(

        worker

    )



    score = (

        skill*0.4

        +

        availability*0.2

        +

        reliability*0.2

        +

        quality*0.2

    )


    return round(

        score,

        2

    )



def explain_match(worker, job):


    return {

        "Skill Compatibility":

            skill_matching(worker,job),


        "Availability":

            availability_score(worker),


        "Reliability":

            reliability_score(worker),


        "Quality Prediction":

            quality_prediction(worker),


        "Final AI Confidence":

            calculate_match(worker,job)

    }
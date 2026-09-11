from services.impact_service import (
    get_project_impact
)



def calculate_social_impact_score(

        project_id

):


    impact = get_project_impact(

        project_id

    )


    if not impact:

        return 0



    workers = impact.get(

        "workers_supported",

        0

    )


    hours = impact.get(

        "working_hours",

        0

    )


    income = impact.get(

        "income_generated",

        0

    )



    employment_score = min(

        workers / 3,

        100

    )



    working_score = min(

        hours / 100,

        100

    )



    economic_score = min(

        income / 1000,

        100

    )



    score = (

        employment_score * 0.4

        +

        working_score * 0.3

        +

        economic_score * 0.3

    )



    return round(score)




def generate_esg_summary(

        project_id

):


    impact = get_project_impact(

        project_id

    )


    if not impact:

        return None



    score = calculate_social_impact_score(

        project_id

    )


    return {


        "score":

            score,


        "workers":

            impact["workers_supported"],


        "hours":

            impact["working_hours"],


        "income":

            impact["income_generated"],


        "message":

        """

        SkillBridge AI creates measurable inclusive

        workforce impact through verified employment,

        community participation and sustainable income.

        """

    }
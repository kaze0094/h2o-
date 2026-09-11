"""
Quality Risk Intelligence Engine
"""


def calculate_project_risk(

        project

):


    quality = project.get(

        "quality_score",

        95

    )


    if quality >=90:

        level="LOW"


    elif quality>=75:

        level="MEDIUM"


    else:

        level="HIGH"



    return {


        "risk":level,


        "quality_score":quality,


        "recommendation":

        "Continue monitoring"


    }
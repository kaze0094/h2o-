def calculate_project_risk(project):


    defect = project.get(
        "defect_rate",
        0
    )


    quality = project.get(
        "quality_score",
        0
    )


    if defect < 2 and quality >=95:

        return {

            "risk":

            "Low",

            "score":

            95

        }


    elif defect <5:

        return {

            "risk":

            "Medium",

            "score":

            70

        }


    else:

        return {

            "risk":

            "High",

            "score":

            40

        }
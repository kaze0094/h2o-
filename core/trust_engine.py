def calculate_trust_intelligence(entity):


    trust_score = entity.get(
        "trust_score",
        0
    )


    if trust_score >= 90:

        level = "High Trust"

        risk = "Low"


    elif trust_score >= 70:

        level = "Medium Trust"

        risk = "Moderate"


    else:

        level = "Low Trust"

        risk = "High"



    return {

        "trust_score":
            trust_score,


        "trust_level":
            level,


        "risk_level":
            risk,


        "signals": [

            "Identity verification completed",

            "Performance history available",

            "Reliability record verified"

        ]

    }
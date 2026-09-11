
def calculate_social_impact(data):

    workers = data.get(
        "workers_supported",
        0
    )


    income = data.get(
        "income_generated",
        0
    )


    hours = data.get(
        "working_hours",
        0
    )


    return {

        "workers":

            workers,


        "income":

            income,


        "working_hours":

            hours,


        "impact_score":

            round(

                workers*0.4

                +

                income/1000*0.3

                +

                hours/100*0.3,

                2

            )

    }
from services.data_loader import load_json



def get_impacts():

    return load_json(
        "impact.json"
    )



def get_project_impact(
    project_id
):

    impacts = get_impacts()


    for impact in impacts:

        if impact["project_id"] == project_id:

            return impact


    return None

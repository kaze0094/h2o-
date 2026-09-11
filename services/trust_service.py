from services.data_loader import load_json



def get_trust_data():

    return load_json(
        "trust.json"
    )



def get_entity_trust(
    entity_id
):

    data = get_trust_data()


    for item in data:

        if item["entity_id"] == entity_id:

            return item


    return None

from services.data_loader import load_json



def get_enterprises():

    return load_json(
        "enterprises.json"
    )



def get_enterprise(
    enterprise_id
):

    enterprises = get_enterprises()


    for enterprise in enterprises:

        if enterprise["enterprise_id"] == enterprise_id:

            return enterprise


    return None



def get_enterprise_trust(
    enterprise_id
):

    enterprise = get_enterprise(
        enterprise_id
    )


    if enterprise:

        return enterprise["trust_score"]


    return 0

from services.data_loader import load_json



# =====================================
# LEGACY
# =====================================


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



# =====================================
# ENTERPRISE V2
# =====================================


def get_enterprises_v2():

    return load_json(
        "enterprises_v2.json"
    )



def get_enterprise_v2(
        enterprise_id
):

    enterprises = get_enterprises_v2()


    for enterprise in enterprises:


        if enterprise["enterprise_id"] == enterprise_id:

            return enterprise


    return None



def get_enterprise_profile(

        enterprise_id

):


    enterprise = get_enterprise_v2(

        enterprise_id

    )


    if not enterprise:

        return None



    return {

        "name":

            enterprise["profile"]["name"],


        "industry":

            enterprise["profile"]["industry"],


        "trust_score":

            enterprise["trust"]["score"],


        "verification":

            enterprise["trust"]["verification"]

    }
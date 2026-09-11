from services.trust_service import (
    get_entity_trust
)


from core.trust_engine import (
    calculate_trust_intelligence
)



def get_trust_intelligence(
    entity_id
):


    entity = get_entity_trust(
        entity_id
    )


    if not entity:

        return None



    data = {


        "trust_score":

        entity["trust_score"]


    }



    return calculate_trust_intelligence(
        data
    )
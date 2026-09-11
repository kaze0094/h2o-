from services.data_loader import load_json



def get_communities():

    return load_json(
        "communities.json"
    )



def get_community(
    community_id
):

    communities = get_communities()


    for community in communities:

        if community["community_id"] == community_id:

            return community


    return None

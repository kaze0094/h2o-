import json
from pathlib import Path


DATA_FILE = Path(
    "data/enterprises.json"
)



def load_enterprises():

    with open(
        DATA_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)



def get_all_enterprises():

    return load_enterprises()



def get_enterprise(company_id):

    enterprises = load_enterprises()


    for company in enterprises:

        if company["enterprise_id"] == company_id:

            return company


    return None



def get_verified_enterprises():

    enterprises = load_enterprises()


    return len(
        [
            e
            for e in enterprises
            if e["status"]=="verified"
        ]
    )



def get_average_trust_score():

    enterprises = load_enterprises()


    if not enterprises:

        return 0


    score = sum(
        e["trust_score"]
        for e in enterprises
    )


    return round(
        score / len(enterprises),
        1
    )

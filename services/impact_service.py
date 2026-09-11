import json
from pathlib import Path


DATA_FILE = Path(
    "data/impact.json"
)



def load_impacts():

    with open(
        DATA_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)



def get_project_impact(
    project_id
):

    impacts = load_impacts()


    for item in impacts:

        if item["project_id"] == project_id:

            return item


    return None



def get_total_income():

    data = load_impacts()


    return sum(
        x["income_generated"]
        for x in data
    )

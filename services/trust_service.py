import json
from pathlib import Path


DATA_FILE = Path(
    "data/trust.json"
)



def load_trust():

    with open(
        DATA_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)



def get_enterprise_trust(
    enterprise_id
):

    data = load_trust()


    for item in data:

        if item["enterprise_id"] == enterprise_id:

            return item


    return None
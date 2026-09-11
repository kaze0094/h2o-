import json
from pathlib import Path


BASE_PATH = Path("data")


def load_json(filename):

    file_path = BASE_PATH / filename


    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)

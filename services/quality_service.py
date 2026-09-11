import json
from pathlib import Path


DATA_FILE = Path(
    "data/projects.json"
)



def load_projects():

    with open(
        DATA_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)



def get_project(project_id):

    projects = load_projects()


    for project in projects:

        if project["project_id"] == project_id:

            return project


    return None



def get_quality_score(project_id):

    project = get_project(
        project_id
    )

    if project:

        return project["quality_score"]

    return 0



def get_quality_risk(project_id):

    project = get_project(
        project_id
    )

    if project:

        return project["risk_level"]

    return "Unknown"



def get_completion_rate(project_id):

    project = get_project(
        project_id
    )

    if project:

        return project["completion"]

    return 0
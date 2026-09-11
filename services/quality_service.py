from services.data_loader import load_json



def get_projects():

    return load_json(
        "projects.json"
    )



def get_project(
    project_id
):

    projects = get_projects()


    for project in projects:

        if project["project_id"] == project_id:

            return project


    return None

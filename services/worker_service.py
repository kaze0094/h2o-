from services.data_loader import load_json



# =====================================
# LEGACY DATA
# =====================================

def get_all_workers():

    return load_json(
        "workers.json"
    )



def get_worker(worker_id):

    workers = get_all_workers()


    for worker in workers:

        if worker["worker_id"] == worker_id:

            return worker


    return None



def get_workers_by_community(community_id):

    workers = get_all_workers()


    return [

        worker

        for worker in workers

        if worker["community_id"] == community_id

    ]



# =====================================
# DIGITAL TWIN V2
# =====================================


def get_all_workers_v2():

    return load_json(
        "workers_v2.json"
    )



def get_worker_v2(worker_id):

    workers = get_all_workers_v2()


    for worker in workers:

        if worker["worker_id"] == worker_id:

            return worker


    return None



def get_worker_profile(worker_id):

    worker = get_worker(worker_id)


    if not worker:

        return None


    return {

        "name":

            worker["name"],


        "skills":

            worker["skills"],


        "performance":

            worker["performance"],


        "trust":

            worker["trust"]

    }



# =====================================
# AI CAPABILITY FUNCTIONS
# =====================================


def get_worker_capabilities(worker_id):


    worker = get_worker_v2(
        worker_id
    )


    if not worker:

        return []



    return worker.get(

        "capabilities",

        []

    )



def get_worker_skill_score(

        worker_id,

        skill_name

):


    capabilities = get_worker_capabilities(

        worker_id

    )


    for skill in capabilities:


        if skill["skill"] == skill_name:

            return skill["score"]


    return 0



def get_worker_skill_evidence(

        worker_id,

        skill_name

):


    capabilities = get_worker_capabilities(

        worker_id

    )


    for skill in capabilities:


        if skill["skill"] == skill_name:

            return skill.get(

                "evidence",

                []

            )


    return []
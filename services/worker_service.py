from services.data_loader import load_json



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



def get_workers_by_community(
    community_id
):

    workers = get_all_workers()


    return [

        worker

        for worker in workers

        if worker["community_id"]
        ==
        community_id

    ]



def get_worker_profile(worker_id):

    worker = get_worker(
        worker_id
    )


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

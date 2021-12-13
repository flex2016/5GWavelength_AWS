from Alsvin-5GAPI.extensions import celery


@celery.task
def dummy_task():
    return "OK"

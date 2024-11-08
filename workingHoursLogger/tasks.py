#from .celery_app import make_celery, celery_app
from celery.utils.log import get_task_logger
from celery import shared_task
import time


# When __name__ is used inside a module, it contains the name of that module (e.g., "tasks")
logger = get_task_logger(__name__)

@shared_task(ignore_result=False)
def longtime_add():
    logger.info('Got request...')
    time.sleep(7)
    logger.info('Finished...')
    return 10

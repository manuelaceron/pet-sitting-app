#from .celery_app import make_celery, celery_app
from celery.utils.log import get_task_logger
from celery import shared_task
import time
from flask_mail import Message
from .app import mail
from .config import Config


# When __name__ is used inside a module, it contains the name of that module (e.g., "tasks")
logger = get_task_logger(__name__)

@shared_task(ignore_result=False)
def longtime_add(subject, body):
    logger.info('Got request...')
    #time.sleep(7)
    mail_message = Message(
                            subject=subject, 
                            sender = Config.MAIL_USERNAME, 
                            recipients = ['manuela.ceron@uao.edu.co'])
    mail_message.body = body
    mail.send(mail_message)
    logger.info('Finished...')

    return "Mail has sent"

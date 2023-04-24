from requests.cookies import RequestsCookieJar
from celery import Celery
from celery.schedules import crontab

import faapi

from tasks import send_notifications


app = Celery('workers', broker='redis://memdb:6379/0')


notification_mapping = {
    'S': 'submission',
    'C': 'comments',
    'F': 'favorites',
    'J': 'journal',
    'N': 'messages',
}


app.task(send_notifications, name='Fetch notifications amount')


@app.on_after_configure.connect
def setup_schedule(sender, **kwargs):
    sender.add_periodic_task(
        crontab(second=5), send_notifications.s()
    )

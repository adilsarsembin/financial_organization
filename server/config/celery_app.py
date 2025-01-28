import os

from celery import Celery
from kombu import Exchange, Queue

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('financial-organization-celery')

app.config_from_object('django.conf:settings', namespace="CELERY")
app.autodiscover_tasks()

app.conf.task_queues = [
    Queue(
        'financial-organization-celery',
        Exchange('financial-organization-celery'),
        routing_key='financial-organization-celery'
    ),
]


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f"Request: {self.request!r}")

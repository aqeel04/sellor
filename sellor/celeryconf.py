import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sellor.settings')

app = Celery('sellor')

CELERY_TIMEZONE = 'UTC'

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

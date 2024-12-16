from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'docker_celery.settings')

app = Celery('docker_celery')
app.config_from_object('django.conf:settings', namespace="CELERY")
app.autodiscover_tasks()
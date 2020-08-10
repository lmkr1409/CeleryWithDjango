from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CeleryAsyncTaskForDjango.settings')
#https://stackoverflow.com/questions/45744992/celery-raises-valueerror-not-enough-values-to-unpack
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')
app = Celery('CeleryAsyncTaskForDjango')

# Using a string here means the worker will not have to pickle the object when using Windows.
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
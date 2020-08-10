from django.utils import timezone
from celery.decorators import task
from time import sleep

@task(name="async_model_task")
def async_model_task():
    with open("output.txt",'w') as f:
        f.write("\ntask started: {}\n".format(timezone.localtime()))
        sleep(10)
        f.write("task finished: {}".format(timezone.localtime()))
    return ""
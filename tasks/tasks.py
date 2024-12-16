from time import sleep
from .models import Task
from celery import shared_task

@shared_task
def long_running_task(task_id):
    task = Task.objects.get(id=task_id)
    sleep(10)
    task.completed = True
    task.save()
    return f"Task {task_id} completed successfully!"
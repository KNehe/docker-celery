from django.shortcuts import render
from django.http import JsonResponse
from .models import Task
from .tasks import long_running_task

def create_task(request):
    task = Task.objects.create(
        title="Sample Background Task",
        description="This task will run in the background"
    )
    result = long_running_task.delay(task.id)
    return JsonResponse({
        'task_id': task.id, 
        'celery_task_id': result.id,
        'status': 'Task queued'
    })

def list_tasks(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})
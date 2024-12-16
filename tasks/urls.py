from . import views
from django.urls import path

urlpatterns = [
    path('create/', views.create_task, name='create_task'),
    path('list/', views.list_tasks, name='list_tasks'),
]
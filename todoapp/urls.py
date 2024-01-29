from django.urls import path
from .views import TaskListView, TaskDetailView 

urlpatterns = [
    path("task/", TaskListView.as_view(), name="TaskListView"),
    path("details/<int:pk>",TaskDetailView.as_view(), name="TaskDetailView"),
    
]
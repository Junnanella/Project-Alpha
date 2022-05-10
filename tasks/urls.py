from django.urls import path
from .views import TaskCreateView, TaskListView

# app_name = "tasks"

urlpatterns = [
 path("create/", TaskCreateView.as_view(), name="create_task"),
 path("mine/", TaskListView.as_view(), name="show_my_tasks")
]
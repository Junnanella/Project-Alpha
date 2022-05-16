from django.urls import path
from .views import ProjectListView, ProjectDetailView, ProjectCreateView, index

# app_name = "project"

urlpatterns = [
    path("projects/mine/", ProjectListView.as_view(), name="list_projects"),
    path(
        "projects/<int:pk>/", ProjectDetailView.as_view(), name="show_project"
    ),
    path(
        "projects/create/", ProjectCreateView.as_view(), name="create_project"
    ),
    path("home/", index, name="index"),
]

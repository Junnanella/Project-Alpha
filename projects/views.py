# from django.shortcuts import render
from django.views.generic import ListView
from .models import Project
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = "projects/project_list.html"
    context_object_name = "projects"

    def get_queryset(self):
        return Project.objects.filter(members=self.request.user)

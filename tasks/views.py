from django.shortcuts import redirect
from django.urls import reverse_lazy
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

# Create your views here.


class TaskCreateView(LoginRequiredMixin,CreateView):
    model = Task
    template_name = "tasks/task_create.html"
    fields = ["name", "start_date", "due_date", "project", "assignee"]

    def form_valid(self, form):
        task = form.save(commit=False)
        task.save()
        return redirect("project:show_project", pk=task.project.pk)


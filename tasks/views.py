from cmath import log
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView

# Create your views here.


class TaskCreateView(LoginRequiredMixin,CreateView):
    model = Task
    template_name = "tasks/task_create.html"
    fields = ["name", "start_date", "due_date", "project", "assignee"]

    def form_valid(self, form):
        task = form.save(commit=False)
        task.save()
        return redirect("show_project", pk=task.project.pk)


class TaskListView(LoginRequiredMixin,ListView):
    model = Task
    template_name = "tasks/tasks_list.html"
    context_object_name = "tasks"

    def get_queryset(self):
        return Task.objects.filter(assignee=self.request.user)
    
class TaskUpdateView(LoginRequiredMixin,UpdateView):
    model = Task
    template_name = "tasks/tasks_list.html"
    fields = ["is_complete"]

    success_url = reverse_lazy("show_my_tasks")
        

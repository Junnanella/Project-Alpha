from django.views.generic import ListView, DetailView, CreateView
from .models import Project
from tasks.models import Task
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from datetime import date, datetime
import calendar

# Create your views here.


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = "projects/project_list.html"
    context_object_name = "projects"

    def get_queryset(self):
        return Project.objects.filter(members=self.request.user)


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = "projects/project_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = "projects/project_create.html"
    fields = ["name", "description", "members"]

    def form_valid(self, form):
        project = form.save(commit=False)
        project.save()
        form.save_m2m()
        return redirect("show_project", pk=project.id)


# view for home page
def index(request):
    # get data from models to pass into context data
    # all projects logged in user is part of
    user_projects = Project.objects.filter(members=request.user)
    # all of users tasks
    user_tasks = Task.objects.filter(assignee=request.user)

    current_date = date.today()
    current_day = calendar.day_name[current_date.weekday()]
    current_hour = datetime.now().hour

    # context data to pass to render
    context = {
        "user_projects": user_projects,
        "user_tasks": user_tasks,
        "current_day": current_day,
        "current_date": current_date,
        "current_hour": current_hour
    }

    return render(request, "projects/index.html", context=context)

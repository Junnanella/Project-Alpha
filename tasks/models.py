from django.db import models
from projects.models import Project
from django.conf import settings

USER_MODEL = settings.AUTH_USER_MODEL

# Create your models here.


class Task(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    due_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    project = models.ForeignKey(
        Project, related_name="tasks", on_delete=models.CASCADE
    )
    assignee = models.ForeignKey(
        USER_MODEL, related_name="tasks", null=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.name

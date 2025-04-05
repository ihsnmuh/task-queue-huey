from django.contrib.auth.models import User
from django.db import models

from core.models import BaseModels


class Task(BaseModels):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    due_at = models.DateTimeField()  # deadline

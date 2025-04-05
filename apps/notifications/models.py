from django.db import models

from apps.tasks.models import Task
from core.models import BaseModels


class Notification(BaseModels):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    message = models.TextField()
    sent_at = models.DateTimeField(null=True, blank=True)
    success = models.BooleanField(default=False)

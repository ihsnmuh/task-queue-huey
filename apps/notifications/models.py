from django.db import models

from apps.tasks.models import Task
from core.models import BaseModels


class Notification(BaseModels):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    message = models.TextField()
    sent_at = models.DateTimeField(null=True, blank=True)  # waktu pengiriman
    success = models.BooleanField(default=False)           # true jika sudah muncul
    is_scheduled = models.BooleanField(default=False)      # dipakai untuk tracking Huey
    
    def __str__(self):
        return f"Notif: {self.message[:30]}... | Task: {self.task.title}"

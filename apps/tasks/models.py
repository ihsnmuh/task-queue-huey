from django.contrib.auth.models import User
from django.db import models

from core.models import BaseModels


class Task(BaseModels):
    TASK_STATUS = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('overdue', 'Overdue'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=TASK_STATUS, default='pending')
    due_at = models.DateTimeField()  # deadline
    is_notified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} - {self.user}"

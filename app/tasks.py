from huey.contrib.djhuey import task

from apps.notifications.models import Notification
from apps.tasks.models import Task
from django.utils import timezone


@task()
def schedule_notification_task(task_id):
    from .methods import schedule_notification
    task = Task.objects.get(id=task_id)
    schedule_notification(task)
    
    
@task()
def send_notification_task(notification_id):
    try:
        notif = Notification.objects.get(id=notification_id)
        notif.sent_at = timezone.now()
        notif.success = True
        notif.save()
        print(f"[Huey] Notifikasi dikirim: {notif.message}")
    except Notification.DoesNotExist:
        print(f"[Huey] Notification ID {notification_id} tidak ditemukan.")

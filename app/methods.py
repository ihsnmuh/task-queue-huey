from datetime import timedelta
from django.utils import timezone
from django.utils.timezone import localtime
from apps.notifications.models import Notification
from .tasks import send_notification_task


def schedule_notification(task, minutes=2):
    notify_at = task.due_at - timedelta(minutes=minutes)
    now = localtime(timezone.now())
    
    print(f"[DEBUG] now: {now}")
    print(f"[DEBUG] task.due_at: {task.due_at}")
    print(f"[DEBUG] notify_at: {notify_at}")
    
    notif = Notification.objects.create(
        task=task,
        message=f"Reminder: Tugas '{task.title}' akan jatuh tempo pada {task.due_at.strftime('%Y-%m-%d %H:%M')}",
        sent_at=None,
        success=False
    )
    
    delay_seconds = (notify_at - now).total_seconds()
    
    print(f"[Huey] Notifikasi {task.title} dijadwalkan untuk {delay_seconds} detik dari sekarang.")

    if delay_seconds > 0:
        send_notification_task.schedule(args=(notif.id,), delay=delay_seconds)
    else:
        print(f"[Huey] Jadwal reminder sudah lewat, kirim langsung.")
        send_notification_task(notif.id) 
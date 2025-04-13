from datetime import timedelta

from django.utils import timezone
from django.utils.timezone import localtime

from apps.notifications.models import Notification
from apps.tasks.models import Task

from .tasks import send_notification_task


def schedule_notification(task, minutes=2):
    notify_at = task.due_at - timedelta(minutes=minutes)
    now = localtime(timezone.now())
    due_at_local = localtime(task.due_at)

    print(f"[DEBUG] now: {now}")
    print(f"[DEBUG] task.due_at: {task.due_at}")
    print(f"[DEBUG] notify_at: {notify_at}")

    notif = Notification.objects.create(
        task=task,
        message=f"Reminder: Tugas '{task.title}' akan jatuh tempo pada {due_at_local.strftime('%Y-%m-%d %H:%M')}",
        sent_at=None,
        success=False,
    )

    delay_seconds = (notify_at - now).total_seconds()

    print(
        f"[Huey] Notifikasi {task.title} dijadwalkan untuk {delay_seconds} detik dari sekarang."
    )

    if delay_seconds > 0:
        send_notification_task.schedule(args=(notif.id,), delay=delay_seconds)
    else:
        print(f"[Huey] Jadwal reminder sudah lewat, kirim langsung.")
        send_notification_task(notif.id)


def send_notification(notification_id):
    try:
        notif = Notification.objects.get(id=notification_id)
        notif.sent_at = timezone.now()
        notif.success = True
        notif.save()
        print(f"[Huey] Notifikasi dikirim: {notif.message}")
    except Notification.DoesNotExist:
        print(f"[Huey] Notification ID {notification_id} tidak ditemukan.")


def update_status():
    now = localtime(timezone.now())
    overdue_tasks = Task.objects.filter(
        status="pending",
        due_at__lt=now,
    )
    count = overdue_tasks.count()

    for task in overdue_tasks:
        task.status = "overdue"
        task.save()

    print(f"[Huey] Updated {count} task(s) to overdue at {now}")

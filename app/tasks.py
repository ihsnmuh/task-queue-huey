from huey.contrib.djhuey import task

from apps.tasks.models import Task


@task()
def schedule_notification_task(task_id):
    from .methods import schedule_notification

    task = Task.objects.get(id=task_id)
    schedule_notification(task)


@task()
def send_notification_task(notification_id):
    from .methods import send_notification

    send_notification(notification_id=notification_id)

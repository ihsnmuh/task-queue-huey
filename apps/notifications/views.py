from django.views.generic import ListView

from .models import Notification


class NotificationListView(ListView):
    model = Notification
    template_name = "notification_list.html"
    context_object_name = "notifications"

    def get_queryset(self):
        return Notification.objects.filter(
            task__user=self.request.user, success=True
        ).order_by("-sent_at")

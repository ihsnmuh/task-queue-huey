from django.urls import path

from apps.notifications.views import NotificationListView

from . import views

urlpatterns = [
    path("", views.TaskListView.as_view(), name="task_list"),
    path("create/", views.TaskCreateView.as_view(), name="create_task"),
    path("notifications/", NotificationListView.as_view(), name="notification_list"),
]

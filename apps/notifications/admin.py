from django.contrib import admin

from .models import Notification


class NotificationAdmin(admin.ModelAdmin):
    list_display = ("task", "message", "sent_at", "success", "is_scheduled")
    list_filter = ("sent_at", "success", "is_scheduled")
    search_fields = ("task__title", "message")


admin.site.register(Notification, NotificationAdmin)

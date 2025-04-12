from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "due_at", "user", "created_at")
    list_filter = ("created_at", "updated_at")
    search_fields = ("title",)


admin.site.register(Task, TaskAdmin)

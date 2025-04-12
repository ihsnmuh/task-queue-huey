from django.contrib import admin

from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "email", "created_at")
    list_filter = ("created_at", "updated_at")
    search_fields = ("user",)


admin.site.register(Profile, ProfileAdmin)

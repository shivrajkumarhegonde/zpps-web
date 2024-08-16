from django.contrib import admin
from .models import Announcement

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')  # Add any fields you want to display in the admin list view

# Alternatively, you can use this simpler method without the decorator
# admin.site.register(Announcement)

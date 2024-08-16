# activities/admin.py
from django.contrib import admin
from .models import Activity, ActivityImage

class ActivityImageInline(admin.TabularInline):
    model = ActivityImage
    extra = 1

class ActivityAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    inlines = [ActivityImageInline]

admin.site.register(Activity, ActivityAdmin)
admin.site.register(ActivityImage)

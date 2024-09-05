from django.contrib import admin
from .models import MidDayMeal

@admin.register(MidDayMeal)
class MidDayMealAdmin(admin.ModelAdmin):
    list_display = ('sr_no', 'day', 'dish', 'kheer', 'sprouts')
    search_fields = ('day', 'dish')
    list_filter = ('day',)

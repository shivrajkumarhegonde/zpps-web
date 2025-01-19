from django.contrib import admin
from .models import MidDayMeal

@admin.register(MidDayMeal)
class MidDayMealAdmin(admin.ModelAdmin):
    list_display = ('serial_number', 'day', 'food_item', 'kheer', 'sprouts')

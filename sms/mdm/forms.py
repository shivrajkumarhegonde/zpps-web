from django import forms
from .models import MidDayMeal

class MidDayMealForm(forms.ModelForm):
    class Meta:
        model = MidDayMeal
        fields = ['day', 'food_item', 'kheer', 'sprouts']

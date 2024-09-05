from django import forms
from .models import MidDayMeal

class MidDayMealForm(forms.ModelForm):
    class Meta:
        model = MidDayMeal
        fields = ['sr_no', 'day', 'dish', 'kheer', 'sprouts']
        widgets = {
            'kheer': forms.TextInput(attrs={'placeholder': 'Enter kheer details'}),
            'sprouts': forms.TextInput(attrs={'placeholder': 'Enter sprouts details'}),
        }

    # To handle Marathi day names in dropdown
    DAY_CHOICES = [
        ('सोमवार', 'सोमवार'),
        ('मंगळवार', 'मंगळवार'),
        ('बुधवार', 'बुधवार'),
        ('गुरुवार', 'गुरुवार'),
        ('शुक्रवार', 'शुक्रवार'),
        ('शनिवार', 'शनिवार'),
        ('रविवार', 'रविवार'),
    ]

    day = forms.ChoiceField(choices=DAY_CHOICES)

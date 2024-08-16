# activities/forms.py
from django import forms
from .models import Activity, ActivityImage

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['title', 'description']

class ActivityImageForm(forms.ModelForm):
    class Meta:
        model = ActivityImage
        fields = ['image']

ActivityImageFormSet = forms.inlineformset_factory(Activity, ActivityImage, form=ActivityImageForm, extra=5)

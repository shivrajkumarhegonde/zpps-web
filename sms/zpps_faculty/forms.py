from django import forms
from .models import FacultyMember

class FacultyMemberForm(forms.ModelForm):
    class Meta:
        model = FacultyMember
        fields = ['name', 'position', 'bio', 'image']

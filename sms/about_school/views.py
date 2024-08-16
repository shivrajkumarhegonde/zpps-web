# about_school/views.py

from django.shortcuts import render

def about_school_view(request):
    return render(request, 'about_school/about_school.html')

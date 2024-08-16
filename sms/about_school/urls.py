# about_school/urls.py

from django.urls import path
from .views import about_school_view

urlpatterns = [
    path('', about_school_view, name='about_school'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_database, name='student_database'),
]

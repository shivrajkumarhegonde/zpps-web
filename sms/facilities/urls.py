from django.urls import path
from . import views

urlpatterns = [
    path('', views.facilities_view, name='facilities'),
]

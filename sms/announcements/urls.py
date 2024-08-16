# announcements/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.announcements, name='announcements'),
    path('create/', views.create_announcement, name='create_announcement'),
    path('edit/<int:pk>/', views.edit_announcement, name='edit_announcement'),
    path('delete/<int:pk>/', views.delete_announcement, name='delete_announcement'),
]

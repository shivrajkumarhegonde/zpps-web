# activities/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.activity_list, name='activity_list'),
    path('create/', views.create_activity, name='create_activity'),
    path('edit/<int:pk>/', views.edit_activity, name='edit_activity'),
    path('delete/<int:pk>/', views.delete_activity, name='delete_activity'),
]


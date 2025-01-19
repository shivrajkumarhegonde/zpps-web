from django.urls import path
from . import views

app_name = 'mdm'

urlpatterns = [
    path('', views.meal_list, name='meal_list'),
    path('add/', views.meal_add, name='meal_add'),
    path('edit/<int:pk>/', views.meal_edit, name='meal_edit'),
    path('delete/<int:pk>/', views.meal_delete, name='meal_delete'),
]

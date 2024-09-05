from django.urls import path
from . import views

urlpatterns = [
    path('', views.meal_list, name='meal_list'),
    path('add/', views.meal_add, name='meal_add'),
    path('edit/<int:pk>/', views.meal_edit, name='meal_edit'),
    path('<int:pk>/delete/', views.meal_confirm_delete, name='meal_confirm_delete'),
]

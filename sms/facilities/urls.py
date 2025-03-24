from django.urls import path
from . import views

urlpatterns = [
    path('', views.facilities_list, name='facilities_list'),
    path('add/', views.add_facility, name='add_facility'),
    path('update/<int:pk>/', views.update_facility, name='update_facility'),
    path('delete/<int:pk>/', views.delete_facility, name='delete_facility'),
]
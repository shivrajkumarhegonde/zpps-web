from django.urls import path
from . import views

urlpatterns = [
    path('', views.faculty_list, name='zpps_faculty'),  # Corrected view name
    path('create/', views.create_faculty, name='faculty_member_create'),
    path('<int:faculty_id>/', views.update_faculty, name='faculty_member_detail'),  # Corrected view name and parameter
    path('<int:faculty_id>/edit/', views.update_faculty, name='faculty_member_update'),  # Corrected view name and parameter
    path('<int:faculty_id>/delete/', views.delete_faculty, name='faculty_member_delete'),  # Corrected view name and parameter
    path('faculty/', views.faculty_list, name='faculty_list'),
    path('faculty/create/', views.create_faculty, name='create_faculty'),
    path('faculty/update/<int:faculty_id>/', views.update_faculty, name='update_faculty'),
    path('faculty/delete/<int:faculty_id>/', views.delete_faculty, name='delete_faculty'),

]

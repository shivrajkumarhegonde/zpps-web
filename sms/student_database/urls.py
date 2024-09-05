from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_database, name='student_database'),
    path('ebooks/', views.ebook_list, name='ebook_list'),
    path('ebooks/upload/', views.ebook_upload, name='ebook_upload'),
    path('ebooks/delete/<int:ebook_id>/', views.ebook_delete, name='ebook_delete'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('blogs/', views.blog_list, name='blog_list'),
    path('blogs/create/', views.create_blog, name='create_blog'),
    path('blogs/update/<int:blog_id>/', views.update_blog, name='update_blog'),
    path('blogs/delete/<int:blog_id>/', views.delete_blog, name='delete_blog'),

]


# sms/urls.py

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from login import views  # replace <your_app> with the name of your app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),

]

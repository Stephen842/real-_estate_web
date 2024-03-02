from django.urls import path, include 
from django.conf import settings
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
        path('', views.home, name = 'home'),
        path('about/', views.about, name = 'about_us')
        ]

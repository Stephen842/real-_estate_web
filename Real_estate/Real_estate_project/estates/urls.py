from django.urls import path, include 
from django.conf import settings
from .import views
from django.conf.url.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
        path('', views.home, name = 'home'),
        ]
from django.urls import path, include 
from django.conf import settings
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
        path('', views.home, name = 'home'),
        path('about/', views.about, name = 'about_us'),
        path('blog/', views.blog_list, name = 'blog'),
        path('post/<int:pk>/', views.blog_detail, name = 'blog_detail'),
        path('category/<category>/', views.blog_category, name = 'blog_category'),
        path('contact/', views.contact, name = 'contact'),
        path('services/', views.services, name = 'services'),
         path('listings/', views.listings, name = 'listings'),
        path('success/', views.success, name = 'success'),
        ]

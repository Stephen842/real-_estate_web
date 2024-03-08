from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.template import loader
from datetime import datetime

#this part below is importations of modules that will be used for the authentication aspect of this project
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm

#this part is for the blog aspect of this project
from .models import Post, Comment

# Create your views here.
def home(request):
    current_datetime = datetime.now()

    context = {
        'date': current_datetime,
        'title': 'Your Real Estates Developer/ Consultant and Facility Manager',
    }
    return render(request, 'pages/home.html', context)

def about(request):
    context = {
        'title': 'Discover Platform Estates: Your Premier Real Estate Partner',
    }
    return render(request, 'pages/about.html', context)


def blog_list(request):
    posts = Post.objects.all().order_by('-date_created')

    context = {
                'posts': posts,
                'title': 'Property Insights: Expert Tips, Trends, and Stories'
            }
    return render(request, 'pages/blog.html', context)

def blog_detail(request, pk):
    posts = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)

    context = {
            'posts': posts,
            'comments': comments,
            }
    return render(request, 'pages/blog_detail.html', context)

def blog_category(request, category):
    posts = Post.objects.filter(categories__name__contains=category).order_by('-date_created')

    context = {
            'category': category,
            'posts': posts,
            }
    return render(request, 'pages/blog_category.html', context)

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
from .forms import CommentForm

# Create your views here.
def home(request):
    current_datetime = datetime.now()
    posts = Post.objects.all().order_by('-date_created')

    context = {
        'date': current_datetime,
        'title': 'Your Real Estates Developer/ Consultant and Facility Manager',
        'posts': posts,
    }
    return render(request, 'pages/home.html', context)

def about(request):
    current_datetime = datetime.now()
    posts = Post.objects.all().order_by('-date_created')
    
    context = {
        'title': 'Discover Platform Estates: Your Premier Real Estate Partner',
        'posts': posts,
        'date': current_datetime,
    }
    return render(request, 'pages/about.html', context)


def blog_list(request):
    current_datetime = datetime.now()
    posts = Post.objects.all().order_by('-date_created')

    context = {
                'posts': posts,
                'title': 'Property Insights: Expert Tips, Trends, and Stories',
                'date': current_datetime,
            }
    return render(request, 'pages/blog.html', context)

def blog_detail(request, pk):
    current_datetime = datetime.now()
    post = Post.objects.get(pk=pk)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                        author = form.cleaned_data['author'],
                        body = form.cleaned_data['body'],
                        post = post,
                    )
            comment.save()
            return redirect(request.path_info)

    comments = Comment.objects.filter(post=post)
    context = {
            'post': post,
            'comments': comments,
            'date': current_datetime,
            }
    return render(request, 'pages/blog_detail.html', context)

def blog_category(request, category):
    posts = Post.objects.filter(categories__name__contains=category).order_by('-date_created')
    current_datetime = datetime.now()
    
    context = {
            'category': category,
            'posts': posts,
            'date': current_datetime,
            }
    return render(request, 'pages/blog_category.html', context)

def contact(request):
    current_datetime = datetime.now()
    #mapbox_access_token = 'pk.eyJ1Ijoic3RlcGhlbjg0MiIsImEiOiJjbHR3dnJuZXUwM2J5MmxvZDZ2dm54NTJ1In0.MUhZBdZhDshLPc1uTHp8yw'
    
    context = {
        'date': current_datetime,
        'title': 'Have Questions? Contact Platform Estates',
        #'mapbox_access_token': mapbox_access_token,
    }
    return render(request, 'pages/contact.html', context)


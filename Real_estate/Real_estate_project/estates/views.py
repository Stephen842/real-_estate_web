from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.template import loader
from datetime import datetime
from django.core.mail import send_mail


#this part below is importations of modules that will be used for the authentication aspect of this project
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm

#this part is for the blog aspect of this project
from .models import Post, Comment, Contact, Property, PropertyContact
from .forms import CommentForm, ContactForm, NewsletterForm, PropertyForm, PropertyContactForm

# Create your views here.
def home(request):
    current_datetime = datetime.now()
    posts = Post.objects.all().order_by('-date_created')
    
    if request.method  == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
        
        return render(request, 'pages/success.html')
    newsletter = NewsletterForm()

    context = {
        'date': current_datetime,
        'title': 'Your Real Estates Developer/ Consultant and Facility Manager',
        'posts': posts,
        'newsletter': newsletter,
    }
    return render(request, 'pages/home.html', context)

def about(request):
    current_datetime = datetime.now()
    posts = Post.objects.all().order_by('-date_created')
    newsletter = NewsletterForm()
    context = {
        'title': 'Discover Platform Estates: Your Premier Real Estate Partner',
        'posts': posts,
        'date': current_datetime,
        'newsletter': newsletter,
    }
    return render(request, 'pages/about.html', context)


def blog_list(request):
    current_datetime = datetime.now()
    posts = Post.objects.all().order_by('-date_created')
    newsletter = NewsletterForm()
    context = {
                'posts': posts,
                'title': 'Property Insights: Expert Tips, Trends, and Stories',
                'date': current_datetime,
                'newsletter': newsletter,
            }
    return render(request, 'pages/blog.html', context)

def blog_detail(request, pk):
    current_datetime = datetime.now()
    post = Post.objects.get(pk=pk)
    newsletter = NewsletterForm()

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
            'newsletter': newsletter,
            }
    return render(request, 'pages/blog_detail.html', context)

def blog_category(request, category):
    posts = Post.objects.filter(categories__name__contains=category).order_by('-date_created')
    current_datetime = datetime.now()
    newsletter = NewsletterForm()
    context = {
            'category': category,
            'posts': posts,
            'date': current_datetime,
            'newsletter': newsletter,
            }
    return render(request, 'pages/blog_category.html', context)

def contact(request):
    current_datetime = datetime.now()
    newsletter = NewsletterForm()
    if request.method  == 'POST':
        form = PropertyContactform(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'pages/success.html')
    form = ContactForm()
    
    context = {
        'date': current_datetime,
        'title': 'Have Questions? Contact Platform Estates',
        'form': form,
        'newsletter': newsletter,
    }
    return render(request, 'pages/contact.html', context)

def services(request):
    current_datetime = datetime.now()
    newsletter = NewsletterForm()
    context = {
        'title': 'Discover Your Dream Properties: Platform Real Estate Services Tailored Just for You.',
        'date': current_datetime,
        'newsletter': newsletter,
    }
    return render(request, 'pages/services.html', context)

def listings(request):
    current_datetime = datetime.now()
    newsletter = NewsletterForm()
    property = Property.objects.all().order_by('-date_created')
    context = {
        'title': 'Find Your Ideal land Property in Abuja Nigeria with Platform Estates: Explore Our Premier Listings Today!',
        'date': current_datetime,
        'property': property,
        'newsletter': newsletter,
    }
    return render(request, 'pages/listings.html', context)

def listing_detail(request, pk):
    current_datetime = datetime.now()
    property = Property.objects.get(pk=pk)
    newsletter = NewsletterForm()
    
    if request.method  == 'POST':
        form = PropertyContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'pages/success.html')
    form = PropertyContactForm()

    context = {
            'property': property,
            'date': current_datetime,
            'newsletter': newsletter,
            'form': form,
    }
    return render(request, 'pages/listing_detail.html', context)


def success(request):
    context = {
        'title': 'Message Sent',
    }
    return render(request, 'pages/success.html', context)

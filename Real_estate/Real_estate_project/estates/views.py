from django.shortcuts import render, redirect
from django.contrib import messages

#this part below is importations of modules that will be used for the authentication aspect of this project
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def home(request):
    return render(request, 'pages/home.html')
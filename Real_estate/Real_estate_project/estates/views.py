from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime
#this part below is importations of modules that will be used for the authentication aspect of this project
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def home(request):
    current_datetime = datetime.now()

    context = {
        'date': current_datetime,
    }
    return render(request, 'pages/master.html', context)
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
from .forms import RegisterUserForm


def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            return HttpResponseRedirect(reverse('polls:index'))
    else:
        form = RegisterUserForm()
    return render(request, "authentication/register.html",{"form":form,})
 

def user_login(request):
    context = {
        'user': request.user  
    }
    return render(request, "authentication/login.html", context)

def user_logout(request):
    logout(request)
    messages.success(request,"You have been logged out!")
    return HttpResponseRedirect(reverse('user_auth:login'))
    

def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(
        reverse('user_auth:login')
)
    else:
        login(request, user)
        return HttpResponseRedirect(
            reverse('polls:index')
)

def show_user(request):
    print(request.user.username)
    return render(request, 'authentication/user.html', {
        "username": request.user.username,
        "password": request.user.password
    })



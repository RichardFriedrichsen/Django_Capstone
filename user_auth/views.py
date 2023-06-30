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
    """The function takes form data to register a User in the app. It executes with path: 'register_user/'.
    :param request: The http request Object that is parsed.
    :type request: HttpRequest
    ...
    :return: If form/POST is valid it returns redirects to 'polls:index', if not it returns template "authentication/register.html" with an empty form.
    :rtype: HttpResponse
    """
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
    """The function logs the user out of the app. It executes with path: 'logout_user/'.
    :param request: The http request Object that is parsed.
    :type request: HttpRequest
    ...
    :return: The reverse path of 'user_auth:login' absolute path 'user_auth/'
    :rtype: HttpResponseRedirect
    """
    logout(request)
    messages.success(request,"You have been logged out!")
    return HttpResponseRedirect(reverse('user_auth:login'))
    

def authenticate_user(request):
    """The function is used to authenticate user credentials. It executes with path: 'user_auth/authenticate_user/'.
    :param request: The http request Object that is parsed.
    :type request: HttpRequest
    ...
    :return: If user authentication successful returns reverse path 'polls:index' if not returns the user to 'user_auth:login'
    :rtype: HttpResponseRedirect
    """
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
    """The function is used to show the user credentials. It executes with path: 'show_user/'.
    :param request: The http request Object that is parsed.
    :type request: HttpRequest
    ...
    :return: An HTML template authentication/user.html and a context dictionary for username and password
    :rtype: HTML
    """
    print(request.user.username)
    return render(request, 'authentication/user.html', {
        "username": request.user.username,
        "password": request.user.password
    })



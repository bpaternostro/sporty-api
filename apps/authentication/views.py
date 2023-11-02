from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_list_or_404
from django.db import IntegrityError
from .serializers import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def make_login(request):
    if request.method == "GET":
        return render(request, 'authentication/login.html', {'form': AuthenticationForm()})
    else:
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('homepage')
        else:
            # Return an 'invalid login' error message.
            return render(request, 'authentication/login.html', {'form':AuthenticationForm(), 'error':'Invalid user'})

# Create your views here.
def register(request):
    if request.method == "GET":
        return render(request, 'authentication/register.html', {'form':UserCreationForm()})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request,user)
                
            except IntegrityError:
                return render(request, 'authentication/register.html', {'form':UserCreationForm(), 'error':'user already exist'})
        else:
            return render(request, 'authentication/register.html', {'form':UserCreationForm(), 'error':'password does not martche'})
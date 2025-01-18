from django.shortcuts import render, redirect

from backside.models import Series, Episode, Category, User, Subscription
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username'] 
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You have been teleported"))
            return redirect('home')
        else:
            messages.success(request, ("You are an Imposter"))
            return redirect('login')
    else:
        return render(request, 'SignIn.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("!!!You have been Kicked Out!!!"))
    return redirect('login')
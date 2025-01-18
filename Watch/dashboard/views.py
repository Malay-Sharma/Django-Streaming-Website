from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from backside.models import Series, Episode, Category, User, Subscription

# Create your views here.
def d_home(request):
    return render(request, 'd_home.html', {})

def d_catalog(request):
    alllist = Series.objects.all()
    return render(request, 'd_catalog.html', {'anime': alllist})

def d_user(request):
    alluser = Subscription.objects.all()
    return render(request, 'd_user.html', {'client': alluser})
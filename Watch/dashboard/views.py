from django.shortcuts import render

# Create your views here.
def d_home(request):
    return render(request, 'd_home.html', {})

def d_catalog(request):
    return render(request, 'd_catalog.html', {})

def d_user(request):
    return render(request, 'd_user.html', {})
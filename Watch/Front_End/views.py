from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def listing(request):
    return render(request, 'listing.html', {})
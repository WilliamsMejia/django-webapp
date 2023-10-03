from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request,*args, **kwargs):
    return render(request, "home2.html",{})

def user_pages(request,*args, **kwargs):
    return render(request, "home.html",{})
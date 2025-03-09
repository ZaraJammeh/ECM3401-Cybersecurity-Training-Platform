from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "home/index.html")

def dashboard(request):
    return render(request, "home/dashboard.html")
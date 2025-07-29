from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def index(request):
    if request.user.is_authenticated:
        return redirect(to="dashboard")
    else:
        return render(request, "home/index.html")

@login_required
def dashboard(request):
    return render(request, "home/dashboard.html")
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from user_systems.models import CurrentCourse

def index(request):
    if request.user.is_authenticated:
        return redirect(to="dashboard")
    else:
        return render(request, "home/index.html")

@login_required
def dashboard(request):
    header_text = ""
    if CurrentCourse.objects.filter(user = request.user).exists():
        header_text = "continue with your latest"
    else:
        header_text = "get started with a new"
        
    context = {
        "header_text": header_text
    }
    return render(request, "home/dashboard.html", context)
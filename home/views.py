from django.http import HttpResponse

def index(request):
    return HttpResponse("It's the home page!")

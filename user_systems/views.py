from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

from .forms import LoginForm, SignUpForm

class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = "registration/login.html"
    # if request.method == POST and form data is valid
    def form_valid(self, form):
        return super(CustomLoginView, self).form_valid(form)

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
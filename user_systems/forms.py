from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class LoginForm(AuthenticationForm):
    email = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                 'data-toggle': 'password',
                                                                 'id': 'password',
                                                                 'name': 'password',
                                                                 }))

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    password_conf = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
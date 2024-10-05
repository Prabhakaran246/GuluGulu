from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

class CustomUserForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-contol p-2 rounded-2','placeholder':'Enter your name'}))
    email=forms.CharField(widget=forms.EmailInput(attrs={'class':'form-contol p-2 rounded-2','placeholder':'Enter your email'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form- p-2 rounded-2','placeholder':'Enter your password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-contol p-2 rounded-2','placeholder':'Confirm your password'}))

    class Meta:
        model=User
        fields=['username','email','password1','password2']
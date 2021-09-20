from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from django import forms

class Creater_User(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
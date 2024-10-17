#!/usr/bin/python3

from django import forms
from django.contrib.auth.forms import UserCreationForm
from djamgo.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('usernae', 'email', 'password1', 'password2')

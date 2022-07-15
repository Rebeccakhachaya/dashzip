# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db.models.base import Model
from django.forms import fields
# from authentication.models import Person


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))


    # models    


# class LoginForm(forms.ModelForm):
#       class Meta:
         
#           fields="__all__"





class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "username",
                "class": "form-control"
            }
        ))
    
    phoneNumber= forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "PhoneNumber",
                "class": "form-control"
            }
        ))

        
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    # password2 = forms.CharField(
    #     widget=forms.PasswordInput(
    #         attrs={
    #             "placeholder": "Password check",
    #             "class": "form-control"
    #         }
    #     ))

#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2')

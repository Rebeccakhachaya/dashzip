# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm
import requests
from django.contrib.auth.models import User

import json

# from authentication.models import Person
# from authentication.models import Person


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            url = "https://backend.fulusi.org/api/v1/authenticate/login-user"
            payload = {'username': username,
                       'password': password}
            files = [

            ]
            headers = {
                'Cookie': 'csrftoken=vrQjj8ZSz20G0jEXJ2FrZweLWvisdutD6McVKuAPT5zm0zEKT5BN4ufTaXj33GCW; sessionid=71b15syaag8sm97xl4082ft9pdd1d697'
            }

            # response = requests.request(
            #     "POST", url, headers=headers, data=payload, files=files)
            # # user = authenticate(username=username, password=password)
            # status = response.status_code
            # print(str(response.json()))

            # if status == 200:

                # login(response)
                # msg = response.text
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                print("login sccessful")
            
                # todo: call pearlenergy api to get data using an api key --> authorization token
                return redirect('home')
                # return redirect("home")

            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})
    # return render(request, "accounts/login.html msg})", {"form": form, "msg":



def add_administrator(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        username = request.POST.get("username")
        password=request.POST.get("password")
        phoneNumber=request.POST.get("phoneNumber")
       
        print(username + " " +password+ " "+phoneNumber )
        
        url = "https://backend.fulusi.org/api/v1/authenticate/create_user"
        payload = {'csrftoken':'vrQjj8ZSz20G0jEXJ2FrZweLWvisdutD6McVKuAPT5zm0zEKT5BN4ufTaXj33GCW',
        'username': username,
        'password': password,
        'phoneNumber':phoneNumber
                         }
        files = []
        headers = {}
        response = requests.request(
                 "POST", url, headers=headers, data=payload, files=files
             )
        status = response.status_code
        if  response.status_code == 200:
            print("register successfuly")
            return redirect('login')
        else:
            print("failed")
            print(response)
            return redirect('login')

    else:
        form = SignUpForm()
        return render(request, "accounts/register.html", {"form": form})
                # return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})









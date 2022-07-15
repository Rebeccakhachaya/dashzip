# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from  .views import login_view, add_administrator
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', login_view, name="login"),
    path('add_administrator', add_administrator, name="add_administrator"),
    path('logout/', LogoutView.as_view(), name="logout")
]

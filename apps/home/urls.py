# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path ,re_path
from apps.home import views
from .views import *

urlpatterns = [

    # The home page
    path('home', index, name='home'),

    # Matches any html file
    re_path('home', views.pages, name='pages'),
    # path('/login', pages, name='pages'),

]

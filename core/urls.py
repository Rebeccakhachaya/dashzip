# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("apps.authentication.urls")), # Auth routes - login / register
    path("", include("apps.home.urls")), 
    path("", include("apps.get_order.urls")), 
    path("", include("apps.cart.urls")),  
    # path("", include("apps.cal.urls")),

 


]       
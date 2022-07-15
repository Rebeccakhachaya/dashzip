# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import Person
from apps.authentication.models import Person


admin.site.register(Person)

# Register your models here.

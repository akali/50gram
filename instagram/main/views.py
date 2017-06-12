# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from authe.models import UserProfile


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'main/login.html')
    template = 'main/home.html'
    return render(request, template)


def login_(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        s = "user is registered"
    else:
        s = "user is not registered"
    return render(request, 'main/home.html')


def logout_(request):
    logout(request)
    return index(request)

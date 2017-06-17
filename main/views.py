# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals

import json
import sys
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.db.utils import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from authe.models import UserProfile
from models import Post, Follow, Like


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'main/login.html')
    # posts = request.user.user_posts.all
    posts = Post.objects.all()
    template = 'main/home.html'
    return render(request, template, {"posts": posts})


def login_(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(username=username, password=password)
    try:
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))  # render(request, 'main/home.html')
    except Exception:
        pass
    return render(request, 'main/login.html', {'error_message': 'true'})


def logout_(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


def signup_view(request):
    return render(request, 'main/signup.html')


def signup_(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")

    try:
        user = UserProfile.objects.create_user(username=username, password=password, first_name=first_name,
                                               last_name=last_name)
    except IntegrityError:
        return render(request, 'main/signup.html', {'error_message': 'Username has already taken'})
    login(request, user)
    return HttpResponseRedirect(reverse('index'))


def new_post_view(request):
    return render(request, 'main/new_post.html')


def new_post(request):
    text = request.POST.get("text")
    user = request.user
    post = Post.objects.create_post(user, text)
    return HttpResponseRedirect(reverse('index'))


def get_user(request, username):
    user = get_object_or_404(UserProfile, username=username)
    self = user == request.user

    follows_count = Follow.objects.filter(user1=user, is_active=True).count()
    followers_count = Follow.objects.filter(user2=user, is_active=True).count()
    follows = Follow.objects.filter(user1=user, is_active=True)
    followers = Follow.objects.filter(user2=user, is_active=True)
    context = {'user': user, 'follows_count': follows_count,
               'followers_count': followers_count,
               'follows': follows,
               'followers': followers,
               'self': self}
    if Follow.objects.filter(user1=request.user, user2=user, is_active=True).count() > 0:
        context.update({'following': True})
    return render(request, 'main/profile.html', context)


def new_follow(request, username):
    currentUser = request.user
    user = UserProfile.objects.get(username=username)
    if currentUser != user:
        relation = Follow.objects.create_or_delete_relation(currentUser, user)
    return HttpResponseRedirect(reverse('get_user', args={user}))


def wall(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    follows = Follow.objects.filter(user1=request.user, is_active=True).select_related('user2').all()
    posts = Post.objects.filter(user__in=list(follow.user2 for follow in follows))
    template = 'main/home.html'
    return render(request, template, {"posts": posts})


def like_action(request, post_id):
    post = Post.objects.filter(id=post_id)[0]
    user = request.user
    like = Like.objects.create_or_delete_like(post=post, user=user)
    message = like
    context = {
        'message': str(message)
    }
    return HttpResponse(json.dumps(context), content_type='application/json')

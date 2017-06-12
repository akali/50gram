# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.utils import timezone


class PostManager(models.Manager):
    def create_post(self, user, text):
        post = self.create(user=user, text=text, date=timezone.now())


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, related_name=u'user_posts')
    text = models.CharField(max_length=300, blank=False, default="Hi! I am using 50gram")
    date = models.DateTimeField('Date published', null=False)
    objects = PostManager()


class FollowManager(models.Manager):
    def create_relation(self, user1, user2):
        follow = self.create(user1=user1, user2=user2)


class Follow(models.Model):
    user1 = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, related_name=u'user1_follows')
    user2 = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, related_name=u'user2_followers')
    objects = FollowManager()

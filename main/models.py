# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.utils import timezone


class PostManager(models.Manager):
    def create_post(self, user, text):
        post = self.create(user=user, text=text, date=timezone.now())

    def get(self, *args, **kwargs):
        return super(PostManager, self).get(args, kwargs).filter(is_active=True)

    def all(self):
        return super(PostManager, self).all().filter(is_active=True)


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, related_name=u'user_posts')
    text = models.CharField(max_length=300, blank=False, default="Hi! I am using 50gram")
    date = models.DateTimeField('Date published', null=False)
    is_active = models.BooleanField(default=True)
    objects = PostManager()

    def __str__(self):
        return "Tost: %s said %s! Al endi alp koyayik" % (self.user.username, self.text)


class FollowManager(models.Manager):
    def create_relation(self, user1, user2):
        follow = self.get_or_create(user1=user1, user2=user2)[0]
        return follow

    def create_or_delete_relation(self, user1, user2):
        follow = self.get_or_create(user1=user1, user2=user2)[0]
        follow.is_active = not follow.is_active
        follow.save()
        return follow


class Follow(models.Model):
    user1 = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, related_name=u'user1_follows')
    user2 = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, related_name=u'user2_followers')
    is_active = models.BooleanField(default=False)
    objects = FollowManager()

    def __str__(self):
        return "[%s;%s]" % (self.user1, self.user2)


class LikeManager(models.Manager):
    def create_or_delete_like(self, post, user):
        like = self.get_or_create(post=post, user=user)[0]
        to_like = not like.is_active
        like.is_active = to_like
        like.save()
        return like

    def count(self):
        return super(LikeManager, self).filter(is_active=True).count()


class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, related_name=u'user_likes')
    post = models.ForeignKey(Post, null=False, related_name=u'post_likes')
    is_active = models.BooleanField(default=False)
    objects = LikeManager()

    def __unicode__(self):
        return "Like: %s %s" % (self.user, self.post)

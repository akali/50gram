# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin, AbstractUser


class UserProfileManager(BaseUserManager):
    def create_user(self, username, password=None, first_name=None, last_name=None):
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(username=username)
        user.set_password(password)
        user.set_first_name(first_name)
        user.set_last_name(last_name)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(username, password)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        return "%s %s" % (self.first_name, self.last_name)

    username = models.CharField(max_length=64, blank=False, unique=True, db_index=True, verbose_name=u'Username')
    first_name = models.CharField(max_length=255, blank=True, null=True, verbose_name=u'First name')
    last_name = models.CharField(max_length=255, blank=True, null=True, verbose_name=u'Last name')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False, verbose_name=u'Administrator')
    is_superuser = models.BooleanField(default=False, verbose_name=u'Superuser')
    bio = models.CharField(max_length=255, default="")

    objects = UserProfileManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def full(self):
        return {
            'id': self.id,
            'username': self.username,
            'full_name': self.get_full_name()
        }

    @property
    def is_staff(self):
        return self.is_admin

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def __unicode__(self):
        return self.username

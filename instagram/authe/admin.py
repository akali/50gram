# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from models import UserProfile

class UserAdmin(admin.ModelAdmin):
    fields = ['username', 'first_name', 'bio']
    list_display = ('id', 'username', 'bio', 'get_full_name')
    # list_filter = ['get_full_name']


admin.site.register(UserProfile, UserAdmin)

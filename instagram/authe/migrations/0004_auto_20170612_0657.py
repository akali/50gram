# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-12 06:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authe', '0003_auto_20170612_0646'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={},
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
    ]

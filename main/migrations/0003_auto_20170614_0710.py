# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-14 07:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_follow_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follow',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]

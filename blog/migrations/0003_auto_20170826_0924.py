# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-26 09:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_post_artist'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='release_date',
            field=models.DateTimeField(default=datetime.datetime.now()),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='reviewer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]

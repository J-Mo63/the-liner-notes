# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-26 09:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170826_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='release_date',
            field=models.DateField(),
        ),
    ]

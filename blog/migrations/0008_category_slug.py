# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-09 14:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20161209_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=models.CharField(max_length=100)),
        ),
    ]

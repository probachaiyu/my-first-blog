# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-09 16:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20161209_1752'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='tagname',
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, editable=False, null=True, to='blog.Tag'),
        ),
        migrations.AddField(
            model_name='post',
            name='tags_string',
            field=models.CharField(blank=True, max_length=200, verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='tag',
            name='name',
            field=models.CharField(blank=True, max_length=64, unique=True),
        ),
        migrations.AlterModelTable(
            name='tag',
            table=None,
        ),
    ]

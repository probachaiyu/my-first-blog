# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('comments_text', models.TextField()),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('comments_post', models.ForeignKey(to='blog.Post')),
            ],
        ),
    ]

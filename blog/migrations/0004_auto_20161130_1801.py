# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20161129_1442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='published_date',
        ),
        migrations.AlterField(
            model_name='comments',
            name='comments_text',
            field=models.CharField(max_length=500),
        ),
    ]

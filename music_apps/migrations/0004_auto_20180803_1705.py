# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-03 17:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_apps', '0003_auto_20180801_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='song_url',
            field=models.CharField(default='Paste URL here', max_length=150),
        ),
    ]

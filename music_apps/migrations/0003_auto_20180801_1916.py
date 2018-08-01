# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-08-01 19:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_apps', '0002_auto_20180801_1827'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={},
        ),
        migrations.RemoveField(
            model_name='song',
            name='file_type',
        ),
        migrations.AddField(
            model_name='song',
            name='song_url',
            field=models.CharField(default='Link here', max_length=150),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-29 06:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_remove_movie_viewer_cnt'),
        ('fingo_statistics', '0003_auto_20161129_1447'),
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fingouser',
            name='activities',
            field=models.ManyToManyField(through='fingo_statistics.UserActivity', to='movie.Movie'),
        ),
    ]

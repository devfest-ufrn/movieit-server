# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-27 23:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20171127_2212'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='posterHorizontal',
            new_name='poster_horizontal',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='posterPortrait',
            new_name='poster_portrait',
        ),
    ]

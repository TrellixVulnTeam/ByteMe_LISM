# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-05 15:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20181105_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker',
            name='tags',
            field=models.ManyToManyField(default=None, to='events.Tag'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tags',
            field=models.ManyToManyField(default=None, to='events.Tag'),
        ),
    ]

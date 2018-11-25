# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-25 08:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_remove_userprofile_useremail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='speaker',
            name='id',
        ),
        migrations.AlterField(
            model_name='speaker',
            name='speakerEmail',
            field=models.EmailField(default='xxx@email.com', max_length=254, primary_key=True, serialize=False, unique=True),
        ),
    ]

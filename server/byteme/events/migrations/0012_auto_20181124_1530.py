# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-24 06:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_auto_20181123_0658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='rankingScore',
            field=models.DecimalField(decimal_places=2, default=5.0, max_digits=5),
        ),
    ]

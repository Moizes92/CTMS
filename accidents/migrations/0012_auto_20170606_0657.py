# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-06 03:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accidents', '0011_auto_20170606_0656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accident',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 6, 6, 6, 57, 25, 321470)),
        ),
    ]

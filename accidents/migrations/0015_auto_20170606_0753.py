# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-06 04:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accidents', '0014_auto_20170606_0752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accident',
            name='date_of_accident',
            field=models.DateField(default=datetime.datetime(2017, 6, 6, 7, 53, 6, 368182)),
        ),
    ]

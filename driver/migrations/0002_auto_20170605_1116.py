# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-05 08:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='date_updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 6, 5, 11, 16, 3, 589632), verbose_name='Update Date'),
        ),
    ]

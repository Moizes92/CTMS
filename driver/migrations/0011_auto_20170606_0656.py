# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-06 03:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0010_auto_20170606_0655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='date_updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 6, 6, 6, 56, 48, 764396), verbose_name='Update Date'),
        ),
    ]

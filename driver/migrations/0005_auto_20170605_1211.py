# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-05 09:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0004_auto_20170605_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='date_updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 6, 5, 12, 11, 25, 56812), verbose_name='Update Date'),
        ),
    ]
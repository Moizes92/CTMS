# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-05 08:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gpsdevices', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gpsdevice',
            name='assigned_to',
            field=models.CharField(max_length=30),
        ),
    ]

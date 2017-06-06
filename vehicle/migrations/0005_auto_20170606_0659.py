# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-06 03:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0004_auto_20170606_0657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthlyrecord',
            name='month',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)]),
        ),
        migrations.AlterField(
            model_name='monthlyrecord',
            name='year',
            field=models.IntegerField(choices=[(2016, 2016), (2017, 2017)]),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-06 03:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0003_auto_20170606_0655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthlyrecord',
            name='month',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='monthlyrecord',
            name='year',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

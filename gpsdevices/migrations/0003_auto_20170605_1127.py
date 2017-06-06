# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-05 08:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gpsdevices', '0002_auto_20170605_1116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gpsdevice',
            old_name='phone_num',
            new_name='sim_num',
        ),
        migrations.AlterField(
            model_name='gpsdevice',
            name='purchase_date',
            field=models.DateField(max_length=30),
        ),
        migrations.AlterUniqueTogether(
            name='gpsdevice',
            unique_together=set([('name', 'imei', 'sim_num')]),
        ),
    ]

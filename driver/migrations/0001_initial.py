# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-05 08:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=30, verbose_name='Last Name')),
                ('date_of_birth', models.DateField(default=None, null=True, verbose_name='Date of Birth')),
                ('email', models.EmailField(default=None, max_length=30, verbose_name='E-mail')),
                ('phone', models.CharField(default=None, max_length=14, verbose_name='E-mail')),
                ('address', models.CharField(blank=True, max_length=64, null=True, verbose_name='Address')),
                ('licence_category', models.CharField(max_length=10, null=True, verbose_name='Licence Category')),
                ('licence_id', models.CharField(default=None, max_length=30, verbose_name='Licence ID')),
                ('issuing_authority', models.CharField(default='TRA', max_length=30, verbose_name='Issuing Authority')),
                ('licence_issue_date', models.DateField(default=None, verbose_name='Licence Issue Date')),
                ('licence_expiry_date', models.DateField(default=None, verbose_name='Licence Expiry Date')),
                ('status', models.CharField(default='Inactive', max_length=30, verbose_name='Status')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Date Added')),
                ('date_updated', models.DateTimeField(blank=True, default=datetime.datetime(2017, 6, 5, 11, 1, 15, 117800), verbose_name='Update Date')),
                ('profile_pic', models.ImageField(blank=True, default='drivers/no_image.png', upload_to='drivers/')),
            ],
            options={
                'verbose_name': 'Driver',
                'verbose_name_plural': 'Drivers',
                'ordering': ['first_name', 'last_name'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='driver',
            unique_together=set([('first_name', 'last_name')]),
        ),
    ]

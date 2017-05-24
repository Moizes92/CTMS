# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-22 06:50
from __future__ import unicode_literals

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
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('license_category', models.CharField(max_length=2)),
                ('license_renewal_date', models.DateField()),
                ('image', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='driver',
            unique_together=set([('first_name', 'last_name')]),
        ),
    ]

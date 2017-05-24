from __future__ import unicode_literals

from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


class Vehicle(models.Model):

    plate_num = models.CharField(max_length=9, unique=True, )
    model = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    color = models.CharField(max_length=20, default='white')
    production_year = models.CharField(max_length=20)
    date_of_purchase = models.DateField()
    km_read_at_purchase = models.IntegerField()
    license_renewal_date = models.DateField()
    insurance_renewal_date = models.DateField()
    current_driver = models.CharField(max_length=30)
    status = models.CharField(max_length=30, default='active')

    def __str__(self):
        return self.plate_num


class VehicleStatus(models.Model):

    vehicle = models.ForeignKey(Vehicle)
    status = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)
    date = models.DateField(default=datetime.today)

    def __str__(self):
        return self.status


class VehicleDriver(models.Model):

    vehicle = models.ForeignKey(Vehicle)
    timestamp = models.DateTimeField(auto_now_add=True)
    driver = models.CharField(max_length=20)
    start_date = models.DateField(default=datetime.today)
    end_date = models.DateField(null=True)

    def __str__(self):
        return self.vehicle + " " + self.driver + " "
        + self.start_date + " " + self.end_date

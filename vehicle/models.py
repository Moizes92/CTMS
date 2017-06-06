from __future__ import unicode_literals

from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
from driver.models import Driver


class Vehicle(models.Model):

    licence_num = models.CharField(default=None, max_length=30, verbose_name=_(u'Licence Number'))
    type = models.CharField(default=None, max_length=30, verbose_name=_(u'Type'))
    engine_num = models.CharField(default=None, max_length=30, verbose_name=_(u'Engin Number'))
    registration_date = models.DateField(default=None, null=True, verbose_name=_(u'Registration Date'))
    number_of_seats = models.CharField(default=None, max_length=30, verbose_name=_(u'Number of Seats'))
    color = models.CharField(default=None, max_length=30, verbose_name=_(u'Color'))
    make = models.CharField(default=None, max_length=30, verbose_name=_(u'make'))
    model = models.CharField(default=None, max_length=30, verbose_name=_(u'Model'))
    year = models.CharField(default=None, max_length=30, verbose_name=_(u'Year'))
    body_type = models.CharField(default=None, max_length=30, verbose_name=_(u'Body Type'))
    gas_type = models.CharField(default=None, max_length=30, verbose_name=_(u'Gas Type'))
    date_of_purchase = models.DateField(default=None, max_length=30, verbose_name=_(u'Date of Purchase'))
    km_read_at_purchase = models.IntegerField(default=None, verbose_name=_(u'Km Read at Purchase'))
    licence_renewal_date = models.DateField(default=None, max_length=30, verbose_name=_(u'Licence Renewal Date'))
    insurance_renewal_date = models.DateField(default=None, max_length=30, verbose_name=_(u'Insurance Renewal Date'))

    class Meta:
        ordering = ['licence_num']
        verbose_name = _(u'Vehicle')
        verbose_name_plural = _(u'Vehicles')

    def __str__(self):
        return self.licence_num


class VehicleStatus(models.Model):

    vehicle = models.ForeignKey(Vehicle)
    status = models.CharField(max_length=30, verbose_name=_(u'Status'))
    timestamp = models.DateTimeField(auto_now_add=True)
    date = models.DateField(default=datetime.today)

    def __str__(self):
        return self.status


class VehicleDriver(models.Model):

    vehicle = models.ForeignKey(Vehicle)
    driver = models.ForeignKey(Driver)
    timestamp = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField(default=datetime.today)
    end_date = models.DateField(null=True)

    def __str__(self):
        return self.vehicle + " " + self.driver + " "
        + self.start_date + " " + self.end_date

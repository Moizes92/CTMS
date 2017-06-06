from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
from datetime import datetime


class Driver(models.Model):

    first_name = models.CharField(max_length=30, verbose_name=_(u'First Name'))
    last_name = models.CharField(max_length=30, verbose_name=_(u'Last Name'))
    date_of_birth = models.DateField(default=None, null=True, verbose_name=_(u'Date of Birth'))
    email = models.EmailField(default=None, max_length=30, verbose_name=_(u'E-mail'))
    phone = models.CharField(default=None, max_length=14, verbose_name=_(u'E-mail'))
    address = models.CharField(max_length=64, null=True, blank=True, verbose_name=_(u'Address'))
    licence_category = models.CharField(max_length=10, null=True, verbose_name=_(u'Licence Category'))
    licence_id = models.CharField(default=None, max_length=30, verbose_name=_(u'Licence ID'))
    issuing_authority = models.CharField(default='TRA', max_length=30, verbose_name=_(u'Issuing Authority'))
    licence_issue_date = models.DateField(default=None, verbose_name=_(u'Licence Issue Date'))
    licence_expiry_date = models.DateField(default=None, verbose_name=_(u'Licence Expiry Date'))
    status = models.CharField(default='Inactive', max_length=30, verbose_name=_(u'Status'))
    date_added = models.DateTimeField(auto_now_add=True, verbose_name=_(u'Date Added'))
    date_updated = models.DateTimeField(default=datetime.today(), blank=True, verbose_name=_(u'Update Date'))
    profile_pic = models.ImageField(upload_to='drivers/', blank=True, default='drivers/no_image.png')

    class Meta:
        unique_together = ("first_name", "last_name")
        ordering = ['first_name', 'last_name']
        verbose_name = _(u'Driver')
        verbose_name_plural = _(u'Drivers')

    def __str__(self):
        return self.first_name + " " + self.last_name

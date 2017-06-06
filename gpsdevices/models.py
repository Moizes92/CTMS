from __future__ import unicode_literals

from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
from django.db import models
from vehicle.models import Vehicle


class GPSDevice(models.Model):

    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    imei = models.CharField(max_length=30)
    sim_num = models.CharField(max_length=30)
    purchase_date = models.DateField(max_length=30)
    assigned_to = models.CharField(max_length=30)
    status = models.CharField(max_length=30)

    class Meta:
        unique_together = ("name", "imei", "sim_num")
        ordering = ['purchase_date']
        verbose_name = _(u'GPSDevice')
        verbose_name_plural = _(u'GPSDevices')

    def __str__(self):
        return self.name + " " + self.imei + " " + self.sim_num

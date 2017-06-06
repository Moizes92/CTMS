from __future__ import unicode_literals

from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from driver.models import Driver
from vehicle.models import Vehicle
from django.utils.translation import ugettext_lazy as _


class Accident(models.Model):

    vehicle = models.ForeignKey(Vehicle)
    driver = models.ForeignKey(Driver)
    timestamp = models.DateTimeField(auto_now_add=True)
    date_of_accident = models.DateField(default=datetime.today())
    location = models.CharField(max_length=50, null=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='accidents/', blank=True, default='accidents/no_image.png')

    def __str__(self):
        return self.vehicle
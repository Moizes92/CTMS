from __future__ import unicode_literals

from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from vehicle.models import Vehicle, VehicleStatus, VehicleDriver


class MonthlyRecord(models.Model):

    This_Year = datetime.today().year
    YEAR_CHOICE = [(i, i) for i in range(This_Year-1, This_Year+1)]
    MONTH_CHOICE = [(i, i) for i in range(1, 13)]
    vehicle = models.ForeignKey(Vehicle)
    timestamp = models.DateTimeField(auto_now_add=True)
    year = models.IntegerField(choices=YEAR_CHOICE)
    month = models.IntegerField(choices=MONTH_CHOICE)
    fuel_consumed = models.FloatField()
    cost = models.FloatField()
    km = models.FloatField()

    class Meta:
            unique_together = ("vehicle", "year", "month")

    def __str__(self):
        return str(self.year) + " " + str(self.month)
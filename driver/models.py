from __future__ import unicode_literals

from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


class Driver(models.Model):

    # CHOICES = ['A2', 'A1', 'A', 'B', 'C1', 'C',
    #            'D', 'D1', 'D2', 'D3', 'E', '1']
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(null=True)
    license_category = models.CharField(max_length=2)
    license_renewal_date = models.DateField()
    image = models.CharField(max_length=30)

    class Meta:
        unique_together = ("first_name", "last_name")

    def __str__(self):
        return self.first_name + " " + self.last_name

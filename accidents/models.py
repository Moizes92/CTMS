from __future__ import unicode_literals

from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


class Accident(models.Model):

    vehicle = models.CharField(max_length=50, null=True, blank=True)
    driver = models.CharField(max_length=50, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    date = models.DateField(default=datetime.today())
    cost = models.FloatField()
    description = models.TextField(null=True, blank=True)
    image = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.driver
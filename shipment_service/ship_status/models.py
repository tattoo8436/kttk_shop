# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
# Create your models here.


class ShipmentModel(models.Model):
    # The following are the fields of our table.
    username = models.CharField(max_length=50)
    mobile = models.CharField(max_length=12)
    address = models.CharField(max_length=200)
    checkoutId = models.IntegerField(max_length=10)
    id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=20)

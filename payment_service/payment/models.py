# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
# This is our model for user registration.
class PaymentModel(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    checkoutId = models.IntegerField()
    totalPrice = models.CharField(max_length=10)
    type = models.CharField(max_length=20)
    mobile = models.CharField(max_length=12)
    status = models.CharField(max_length=15)
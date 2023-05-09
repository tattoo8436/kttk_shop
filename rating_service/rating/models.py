# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
# This is our model for user registration.
class Rating(models.Model):
### The following are the fields of our table.
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    productId = models.CharField(max_length=10)
    rating = models.IntegerField()
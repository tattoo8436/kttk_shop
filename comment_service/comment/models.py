# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
# This is our model for user registration.
class comment(models.Model):
### The following are the fields of our table.
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    productId = models.CharField(max_length=10)
    comment = models.CharField(max_length=255)
    ### It will help to print the values.
    def __str__(self):
        return '%s %s %s ' % (self.username, self.productId, self.comment)
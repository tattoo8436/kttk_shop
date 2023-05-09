# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
# This is our model for user registration.
class Product(models.Model):
    id = models.AutoField(primary_key=True, )
    category = models.CharField(max_length=50)
    quantity = models.IntegerField()
    price = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    ### It will help to print the values.
    def __str__(self):
        return '%s %s %s %s %s' % (self.id, self.category,self.name, self.quantity, self.price)
    
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    productId = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)

class Shoes(models.Model):
    id = models.AutoField(primary_key=True)
    productId = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=10)

class Clothes(models.Model):
    id = models.AutoField(primary_key=True)
    productId = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=10)


from __future__ import unicode_literals
from django.db import models
from rest_framework import serializers

class UserModel(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    mobile = models.CharField(max_length=12)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    type = models.CharField(max_length=50, default="NEW")
    def __str__(self):
        return '%s %s %s %s %s %s %s' % (self.fname, self.lname, self.
        email, self.mobile, self.password, self.address, self.type)
    
class UserRole(models.Model):
    email = models.CharField(max_length=50)
    role = models.CharField(max_length=50)


class Role(models.Model):
    role = models.CharField(max_length=50, primary_key=True)

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('role',)

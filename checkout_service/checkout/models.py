from django.db import models


class CheckoutModel(models.Model):
    username = models.CharField(max_length=50)
    cartIds = models.JSONField(max_length=10)
    totalPrice = models.CharField(max_length=10)
    id = models.AutoField(primary_key=True)
    isPay = models.BooleanField(default=False)
from django.db import models

# Create your models here.


class CartModel(models.Model):
    username = models.CharField(max_length=50)
    productId = models.IntegerField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    id = models.AutoField(primary_key=True)
    isActive = models.BooleanField(default=True)

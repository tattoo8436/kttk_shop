from django.db import models

# Create your models here.
class OrderModel(models.Model):
    username = models.CharField(max_length=50)
    productId = models.CharField(max_length=10)
    price = models.CharField(max_length=10)
    quantity = models.CharField(max_length=5)
    id = models.AutoField(primary_key=True)
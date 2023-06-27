from django.db import models


class Keywords(models.Model):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default='New')


class Links(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField()
    status = models.BooleanField(max_length=10, default='New')


class Info(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    reviews = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    series = models.CharField(max_length=100)
    guarantee = models.CharField(max_length=100)
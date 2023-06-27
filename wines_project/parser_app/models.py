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
    characteristic1 = models.CharField(max_length=100)
    characteristic2 = models.CharField(max_length=100)
    characteristic3 = models.CharField(max_length=100)
    characteristic4 = models.CharField(max_length=100)
    characteristic5 = models.CharField(max_length=100)
from django.db import models


class Food(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    stock = models.IntegerField()
    image_url =models.CharField( max_length = 2083)

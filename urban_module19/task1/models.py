from django.db import models


# Create your models here.
class Buyer(models.Model):
    name = models.CharField(max_length=30)
    balance = models.DecimalField(max_digits=20,  decimal_places=10)
    age = models.IntegerField()


class Game(models.Model):
    title = models.CharField(max_length=30)
    cost = models.DecimalField(max_digits=20,  decimal_places=10)
    size = models.DecimalField(max_digits=20,  decimal_places=10)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='games')
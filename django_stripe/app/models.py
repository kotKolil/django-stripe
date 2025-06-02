from email.policy import default

from django.db import models
from django.conf import settings

class Item(models.Model):
    name = models.CharField(max_length=10)
    description = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

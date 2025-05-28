from django.db import models

class Item(models.Model):

    def __str__(self):
        return self.name

    Id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 10)
    description = models.CharField(max_length = 50)
    price = models.IntegerField()
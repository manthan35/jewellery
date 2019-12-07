from django.db import models
from datetime import datetime

class Product(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField()
    specification = models.TextField()
    returns = models.CharField(max_length=300)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return self.name

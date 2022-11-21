from django.db import models

# Create your models here.


class Disaster(models.Model):
    disaster = models.CharField(max_length=30)
    Comment = models.TextField()
    address = models.CharField(max_length=30)
    lat = models.CharField(max_length=30)
    long = models.CharField(max_length=30)

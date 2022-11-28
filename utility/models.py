from django.db import models
from django.contrib.gis.db import models as gismodels
# Create your models here.

class Location(models.Model):
    name=models.CharField(max_length=100,blank=True)
    point=gismodels.PointField(srid=4326,blank=True,null=True)
    
    def __str(self):
        return self.name
    
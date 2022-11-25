
from django.contrib.gis.db import models
from django.db.models import Manager as GeoManager
 
class DisasterType(models.Model):
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name    
    
class DisasterRating(models.Model):
    rating=models.CharField(max_length=30)
    def __str__(self):
        return self.rating   
    
class Disaster(models.Model):
    disaster = models.CharField(max_length=30)
    Comment = models.TextField()
    address = models.CharField(max_length=30)
    lat = models.CharField(max_length=30)
    long = models.CharField(max_length=30)
    
    
    type= models.ForeignKey(DisasterType, on_delete=models.CASCADE,null=True)
    rating=models.ForeignKey(DisasterRating, on_delete=models.CASCADE,null=True)
    
    geom=models.PointField(srid=4326,null=True)
    objects=GeoManager()
    
    def __str__(self):
        return self.disaster

  

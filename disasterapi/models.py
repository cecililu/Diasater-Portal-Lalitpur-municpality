from django.contrib.gis.db import models
from django.db.models import Manager as GeoManager
 
class DisasterType(models.Model):
    name=models.SlugField(max_length=30)
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
     
    type= models.CharField(max_length=20,null=True)
    rating=models.CharField(max_length=20,null=True)
    
    # geom=models.PointField(srid=4326,null=True,default=0)
    objects=GeoManager()
    
    
    def __str__(self):
        return self.disaster

  
class Local(models.Model):                           
    geom = models.MultiPolygonField(srid=4236) 
    type=models.CharField(max_length=20,null=True,blank=True)
    local=models.CharField(max_length=20,null=True,blank=True)
    
    def __str__(self):
        return "Localunit"+str(self.id)
    
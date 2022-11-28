from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from disasterapi.serializer import *

# for main model

class GeoViewSet(viewsets.ModelViewSet):
    queryset = Disaster.objects.all()
    serializer_class = DisasterSerializer
    
class LocalViewSet(viewsets.ModelViewSet):
    queryset = Local.objects.all()
    serializer_class = LocalSerializer
   
class RatingViewSet(viewsets.ModelViewSet):
    queryset = DisasterRating.objects.all()
    serializer_class = DisasterRatingSerializer

class TypeViewSet(viewsets.ModelViewSet):
    queryset = DisasterType.objects.all()
    serializer_class = DisasterTypeSerializer
   
    
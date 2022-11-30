from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from disasterapi.serializer import *

# for main model
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class GeoViewSet(viewsets.ModelViewSet):
    queryset = Disaster.objects.all()
    serializer_class = DisasterSerializer
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    
class LocalViewSet(viewsets.ModelViewSet):
    queryset = Local.objects.all()
    serializer_class = LocalSerializer
   
class RatingViewSet(viewsets.ModelViewSet):
    queryset = DisasterRating.objects.all()
    serializer_class = DisasterRatingSerializer

class TypeViewSet(viewsets.ModelViewSet):
    queryset = DisasterType.objects.all()
    serializer_class = DisasterTypeSerializer
   
    
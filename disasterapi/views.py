from django.shortcuts import render
from rest_framework import viewsets
from .models import Disaster
from disasterapi.serializer import DisasterSerializer
# from rest_framework.authentication import 
# Create your views here.


class GeoViewSet(viewsets.ModelViewSet):
    queryset = Disaster.objects.all()
    serializer_class = DisasterSerializer

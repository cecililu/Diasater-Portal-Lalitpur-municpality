from rest_framework import serializers
from .models import *
from rest_framework_gis.serializers import GeoFeatureModelSerializer
# from rest_framework.ModelSerializer import GeoFeatureModelSerializer

class LocationSerializer(serializers.Serializer):
    lat=serializers.DecimalField(max_digits=22,decimal_places=16)
    long=serializers.DecimalField(max_digits=22,decimal_places=16)
    

class GeoLocationSerializer(GeoFeatureModelSerializer):
     class Meta:
        model = Location
        geo_field='geom'
        fields = "__all__"
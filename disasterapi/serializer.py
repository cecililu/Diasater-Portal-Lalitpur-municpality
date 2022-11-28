from rest_framework import serializers
from .models import *

# from rest_framework.ModelSerializer import GeoFeatureModelSerializer

from rest_framework_gis.serializers import GeoFeatureModelSerializer
class DisasterSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Disaster
        fields = "__all__"

class LocalSerializer(GeoFeatureModelSerializer):
     class Meta:
        model = Local
        geo_field='geom'
        fields ="__all__"

class DisasterTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisasterType
        fields = ('name','id')

class DisasterRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisasterRating
        fields = ('rating','id')             
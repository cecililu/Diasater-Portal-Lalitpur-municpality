from django.contrib import admin
from .models import *

# Register your models here.
from leaflet.admin import LeafletGeoAdmin

class LocationAdmin(LeafletGeoAdmin):
    list_display=('point','name')

admin.site.register(Location,LocationAdmin)
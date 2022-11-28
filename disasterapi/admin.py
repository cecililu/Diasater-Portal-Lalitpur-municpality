from django.contrib import admin
from .models import *
# Register your models here.
from leaflet.admin import LeafletGeoAdmin
class DisasterAdmin(LeafletGeoAdmin):
    list_display=('disaster','lat','long')
class LocalAdmin(LeafletGeoAdmin):
    list_display=('id','local','type')   
    
admin.site.register(DisasterType)
admin.site.register(DisasterRating)
admin.site.register(Disaster,DisasterAdmin)
admin.site.register(Local,LocalAdmin)
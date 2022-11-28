from django.urls import include, path
from rest_framework import routers
from . import views



urlpatterns = [
    
    path('v1/distance', views.getLocationsWithinDistance.as_view()),
    path('v1/buffer', views.getBuffer.as_view()),
    path('v1/shapefile', views.getShapefile.as_view()),
]

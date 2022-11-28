from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from . models import *
from disasterapi.models import *
from . serializer import *
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.measure import D
from osgeo import ogr
import osgeo.osr as osr

class getLocationsWithinDistance(APIView):
    
    def post(self,request):
        print('posted')
        serializer=LocationSerializer(data=request.data)
        
        if serializer.is_valid():
            try:
              
                data=serializer.data
                
                # pnt=Point(data['long'],data['lat'],srid=4326)
                # pnt=ogr.CreateGeometryFromWkt('POINT({} {})'.format(data['long'],data['lat']))
                pnt=GEOSGeometry('POINT({} {})'.format(data['long'],data['lat']),srid=4326)
            
                location=Location.objects.all().filter(point__distance_lte=(pnt, D(km=10000)))
                
                datafrmt=[]
                    
                
                
                for item in location:
                    dic={}
                    name=item.name
                    point=item.point
                    dic={"name":name,"point":str(point)}
                    
                    datafrmt.append(dic)
                    # datafrmt['lat']=item.lat
                    # datafrmt['long']=item.long
                    
                return Response({'distance':str(datafrmt)})
                
            except Exception as e:
                print(e)
        return Response(serializer.errors)                       
                                       
class getBuffer(APIView):
    def post(self,request):
       
        serializer=LocationSerializer(data=request.data)
    
        if serializer.is_valid():
            try:    
                data=serializer.data
                
                # pnt=GEOSGeometry('POINT({} {})'.format(data['long'],data['lat']),srid=4326)
                # print('GEOMETRY',pnt)
                
                pt = ogr.CreateGeometryFromWkt('POINT({} {})'.format(data['long'],data['lat']))
                bufferDistance =500
                poly=pt.Buffer(bufferDistance)
               
                    
                return Response({'bufferPolygon':str(poly)})
                
            except Exception as e:
                print(e)
        return Response(serializer.errors)
import os
from pathlib import Path
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
import fiona
def shapefile():
    driver = ogr.GetDriverByName("ESRI Shapefile")
    data_source = driver.CreateDataSource('./static/disaster1.shp')

    
    srs = osr.SpatialReference()
    srs.ImportFromEPSG(4326)
    
    layer = data_source.CreateLayer("disaster", srs, ogr.wkbPoint)
    
    layer.CreateField(ogr.FieldDefn("Name", ogr.OFTString)) 
    
    layer.CreateField(ogr.FieldDefn("Type", ogr.OFTString)) 
    
    layer.CreateField(ogr.FieldDefn("Rating", ogr.OFTString)) 
    
    layer.CreateField(ogr.FieldDefn("Address", ogr.OFTString))
    
    disaster=Disaster.objects.all()
    # print(type(int(str((disaster[0].rating)))))
    for i in disaster:
        name=str(i.disaster)
        type=str(i.type)
        rating=str(i.rating)
        address=str(i.address)
        
        feature = ogr.Feature(layer.GetLayerDefn())
        feature.SetField("Name",name)
        feature.SetField("Type", type)
        feature.SetField("Rating", rating)
        feature.SetField("Address", address)
        print(str(i.rating))
        wkt = "POINT(%f %f)" %  (float(i.long) , float(i.lat))
        point = ogr.CreateGeometryFromWkt(wkt)
        feature.SetGeometry(point)
        layer.CreateFeature(feature)
        feature = None
    data_source=None
    return 1   
    
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect
from zipfile import ZipFile
import shutil
def getzipped():
    filepath=[
        os.path.join('static/disaster1.shp'),
        os.path.join('static/disaster1.dbf'),
        os.path.join('static/disaster1.prj'),
        os.path.join('static/disaster1.shx'),
    ]
    # path=os.path.join(BASE_DIR,'static')
    for filename in filepath:
        print(filename)
        
    with ZipFile('static/shapefile.zip','w') as zip:
        for file in filepath:
            zip.write(file)

    
from django.http import FileResponse
class getShapefile(APIView):  
    # print(os.path.join(os.path.dirname(BASE_DIR), 'static\disaster.shp'),"++++++++")    
    def get(self,request):
        shapefile()
        getzipped()
        print("_______________________",os.path.join(BASE_DIR,'static\shapefile.zip'))
        return FileResponse(
            open(os.path.join(BASE_DIR,'static\shapefile.zip'), 'rb'),
            as_attachment=True,
            filename='ReportTest.zip'
        )
        
                                          
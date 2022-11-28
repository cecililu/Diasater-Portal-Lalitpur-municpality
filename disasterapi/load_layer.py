import os
from django.contrib.gis.utils import LayerMapping
from . models import Local

local_mapping = {
    'geom': 'MULTIPOLYGON',
    
}
ward_shp=os.path.abspath(os.path.join(os.path.dirname(__file__),'data/Lalitpurshp.shp'))
def run(verbose=True):
    lm=LayerMapping(Local,ward_shp,local_mapping,transform=False,encoding='iso-8859-1')
    lm.save(strict=False,verbose=verbose)
    
from django.conf import settings
from django.conf.urls.defaults import *

urlpatterns = patterns(
    'image_storage.views',
    url(r'(?P<img_id>\d+)$','get_image',name='get_img'),
    
    )

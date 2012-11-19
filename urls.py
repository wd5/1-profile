from django.conf import settings
from django.conf.urls.defaults import *
from django.views.static import serve

urlpatterns = patterns('',
#                       (r'^$','profile.views.index'),
                       (r'^', include('profile.urls')),
                       (r'^img/', include('image_storage.urls')),
                       (r'^blog/', include('blog.urls')),
                       )

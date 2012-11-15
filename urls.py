from django.conf import settings
from django.conf.urls.defaults import *
from django.views.static import serve

urlpatterns = patterns('',
                       (r'^$','profile.views.index'),
#                       (r'^admin/', include(admin.site.urls)),
                       )

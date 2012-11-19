from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns(
    'blog.views',
    url(r'^$', 'index', name='blog'),
    url(r'^create/$', 'create', name='blog-create'),

)

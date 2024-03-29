from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns(
    'blog.views',
    url(r'^$', 'index', name='blog'),
    url(r'^(?P<post_id>\d+)/$', 'post_view', name='blog-post-view'),

    url(r'^admin/$', 'admin', name='blog-admin'),
    url(r'^admin/create/$', 'create', name='blog-create'),
    url(r'^admin/(?P<post_id>\d+)/edit/$', 'edit', name='blog-edit'),

)

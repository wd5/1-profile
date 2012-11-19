from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns(
    'profile.views',
    url(r'^$', 'index', name='home'),
    url(r'^feedback/$', 'index',
        {'template_name': "profile/contacts.html"}, name='feedback'),
    (r'^edit/', include('profile.edit.urls')),
   
)

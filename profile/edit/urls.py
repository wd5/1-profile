from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns(
    'profile.edit.views',
    url(r'^$', 'edit_profile', name='edit-profile'),
    url(r'^work/$', 'edit_work', name='edit-work'),
    url(r'^work/(?P<work_id>\d+)$', 'edit_work', name='edit-work'),
)

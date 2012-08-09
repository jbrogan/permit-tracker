from django.conf.urls import patterns, include, url
from settings import MEDIA_ROOT
from permitTracker.views import trainer, student, session
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'permit.views.home', name='home'),
    # url(r'^permit/', include('permit.foo.urls')),

    (r'^trainers/(\d+)/$', trainer),
    (r'^students/(\d+)/$', student),
    (r'^sessions/(\d+)/$', session),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('userena.urls')),
)

urlpatterns += patterns('',
    (r'^assets/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
)

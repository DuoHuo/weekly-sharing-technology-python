from django.conf.urls import patterns, include, url, static
from django.conf import settings

import xadmin
xadmin.autodiscover()

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

def zsrd_url(regex, view, kwargs=None, name=None, prefix=''):
    url_prefix = '^'+settings.FINGER['api_url_prefix'][1:]
    regex = url_prefix+regex
    return url(regex, view, kwargs, name, prefix)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'finger.views.home', name='home'),
    # url(r'^finger/', include('finger.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^xadmin/', include(xadmin.site.urls)),
    zsrd_url(r'social/', include('social.urls')),
    zsrd_url(r'campus/', include('campus.urls')),
    zsrd_url(r'work/', include('work.urls')),

)

urlpatterns += static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
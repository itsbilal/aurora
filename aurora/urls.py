from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from accounts.views import login 
from communities.views import new as communities_new, enroll as communities_enroll

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'main.views.home', name='home'),
    # url(r'^aurora/', include('aurora.foo.urls')),

    url(r'^login/$', login.as_view(), name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': 'home'}),
    #TODO: Do a signup view

    url(r'^communities/$', 'communities.views.list', name="communities_list"),
    url(r'^communities/new/$', communities_new.as_view(), name="communities_new"),
    url(r'^communities/(?P<id\d+>/$', 'communities.views.details', name='communities_details'),
    url(r'^communities/(?P<id\d+>/enroll/$', communities_enroll.as_view(), name='communities_enroll'),
    url(r'^communities/(?P<id\d+>/manage/$', 'communities.views.manage', name='communities_manage'),


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

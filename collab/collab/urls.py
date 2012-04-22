from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'collab.views.home', name='home'),
    #url(r'^collab/', include('collab.foo.urls')),
    url(r'^survey/$', 'survey.views.index'),
    url(r'^survey/(?P<survey_id>\d+)/$', 'survey.views.detail'),
    url(r'^survey/(?P<survey_id>\d+)/results/$', 'survey.views.results'),
    url(r'^survey/(?P<survey_id>\d+)/vote/$', 'survey.views.vote'),
    url(r'^admin/', include(admin.site.urls)),


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

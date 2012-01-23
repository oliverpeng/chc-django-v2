from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'chc.views.home', name='home'),
    
    (r'^join/', include('chc.apps.join.urls')),
    
    url(r'^what_we_do/$', 'chc.views.what_we_do', name='what-we-do'),
    url(r'^what_we_do/projects/$', 'chc.views.projects', name='what-we-do.projects'),
    url(r'^who_we_are/$', 'chc.views.who_we_are', name='who-we-are'),
    url(r'^churches/$', 'chc.views.churches', name='churches'),
    url(r'^give/$', 'chc.views.give', name='give'),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

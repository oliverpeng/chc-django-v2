from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'chc.views.home', name='home'),
    url(r'^join/$', 'chc.views.join', name='join'),
    url(r'^what_we_do/$', 'chc.views.what_we_do', name='what-we-do'),
    url(r'^where_we_are/$', 'chc.views.where_we_are', name='where-we-are'),
    url(r'^churches/$', 'chc.views.churches', name='churches'),
    url(r'^give/$', 'chc.views.give', name='give'),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'chc.views.home', name='home'),
    
    url(r'^join/$', 'chc.views.join', name='join'),
    url(r'^join/signup/$', 'chc.views.signup', name='signup'),
    url(r'^join/pray/$', 'chc.views.pray', name='pray'),
    url(r'^join/sendprayer/$', 'chc.views.sendprayer', name='sendprayer'),
    url(r'^join/chclive/$', 'chc.views.chclive', name='chclive'),
    url(r'^join/partner$', 'chc.views.partner', name='partner'),
    
    url(r'^what_we_do/$', 'chc.views.what_we_do', name='what-we-do'),
    url(r'^who_we_are/$', 'chc.views.who_we_are', name='who-we-are'),
    url(r'^churches/$', 'chc.views.churches', name='churches'),
    url(r'^give/$', 'chc.views.give', name='give'),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

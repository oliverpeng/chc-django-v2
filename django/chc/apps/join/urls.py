from django.conf.urls.defaults import *

urlpatterns = patterns('views',
    url(r'^join/$', 'chc.views.join', name='join'),
    url(r'^join/signup/$', 'chc.views.signup', name='signup'),
    url(r'^join/signup/thankyou/$', 'chc.views.thanks', name='thanks'),
    url(r'^join/subscribe/$', 'chc.views.subscribe', name='subscribe'),
    url(r'^join/subscribe/thankyou$', 'chc.views.thanks', name='subscribe_thanks'),
    url(r'^join/pray/$', 'chc.views.pray', name='pray'),
    url(r'^join/sendprayer/$', 'chc.views.sendprayer', name='sendprayer'),
    url(r'^join/chclive/$', 'chc.views.chclive', name='chclive'),
    url(r'^join/partner$', 'chc.views.partner', name='partner'),
)
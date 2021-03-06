from django.conf.urls.defaults import *

urlpatterns = patterns('chc.apps.join.views',
    url(r'^$', 'join', name='join'),
    url(r'^signup/$', 'signup', name='join.signup'),
    url(r'^signup/thankyou/$', 'thanks', name='join.thanks'),
    url(r'^subscribe/$', 'subscribe', name='join.subscribe'),
    url(r'^subscribe/thankyou$', 'thanks', name='join.subscribe_thanks'),
    url(r'^pray/$', 'pray', name='join.pray'),
    url(r'^moreways/$', 'moreways', name='join.moreways'),
)
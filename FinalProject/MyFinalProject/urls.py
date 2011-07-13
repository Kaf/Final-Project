from django.conf.urls.defaults import *

urlpatterns = patterns('',
url(r'^home$', 'MyFinalProject.views.home'),
url(r'^company$', 'MyFinalProject.views.listView'),
url(r'^menulist/(?P<id>\d+)$', 'MyFinalProject.views.menuView'),
url(r'^restaurant$', 'MyFinalProject.views.restaurantView'),
url(r'^company/$', 'MyFinalProject.views.listView'),
url(r'^confirm$', 'MyFinalProject.views.displayView'),
#url(r'^$', 'MyFinalProject.views.'),
#url(r'^$', 'MyFinalProject.views.'),
)


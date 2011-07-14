from django.conf.urls.defaults import *

urlpatterns = patterns('',
url(r'^home$', 'MyFinalProject.views.home'),
url(r'^company$', 'MyFinalProject.views.listView'),
url(r'^menulist/(?P<id>\d+)$', 'MyFinalProject.views.menuView'),
url(r'^restaurant/(?P<comp_id>\d+)$', 'MyFinalProject.views.restaurantView'),
url(r'^restaurant/(?P<comp_id>\d+)/check_(?P<check_id>\d+)=(?P<checked>\w+)$', 'MyFinalProject.views.restaurantView'),
url(r'^restaurant/check_(?P<check_id>\d+)=(?P<checked>\w+)$', 'MyFinalProject.views.restaurantView'),
url(r'^company/$', 'MyFinalProject.views.listView'),
url(r'^confirm/(?P<comp_id>\d)$', 'MyFinalProject.views.displayView'),
#url(r'^$', 'MyFinalProject.views.'),
#url(r'^$', 'MyFinalProject.views.'),
)


from django.conf.urls.defaults import *

urlpatterns = patterns('',
url(r'^home$', 'MyFinalProject.views.home'),
<<<<<<< HEAD
url(r'^company$', 'MyFinalProject.views.listView'),
url(r'^menulist/(?P<id>\d+)$', 'MyFinalProject.views.menuView'),
url(r'^menulist$', 'MyFinalProject.views.menuView'),
=======
url(r'^company/$', 'MyFinalProject.views.listView'),
url(r'^menu/(?P<id>\d+)$', 'MyFinalProject.views.menuView'),
#url(r'^$', 'MyFinalProject.views.'),
>>>>>>> 8e085af61d46aee6f28d1bdba66b3034e74e09f6
#url(r'^$', 'MyFinalProject.views.'),
#url(r'^$', 'MyFinalProject.views.'),
)


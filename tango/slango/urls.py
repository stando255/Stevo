from django.conf.urls import patterns, url
from slango import views

urlpatterns = patterns('',
    url(r'^$',views.index, name='index'),
    url(r'^users/(?P<user_name_slug>[\w\-]+)/$', views.slango_main, name='slango_main'),
)
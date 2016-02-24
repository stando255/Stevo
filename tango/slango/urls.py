from django.conf.urls import patterns, url
from slango import views

urlpatterns = patterns('',
    url(r'^$',views.index, name='index'),
    url(r'^slango_main/$',views.slango_main,name='slango_main'))
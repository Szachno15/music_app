
from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    
    #shows all albums
    url(r'^detail/$', views.detail, name='detail'),
    
    #individual pages for Album
    url(r'^detail/(?P<album_id>\d+)/$', views.albums, name='albums') 
]

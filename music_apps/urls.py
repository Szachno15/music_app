
from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    
    #shows all albums
    url(r'^detail/$', views.detail, name='detail'),
    
    #individual pages for Album
    url(r'^detail/(?P<album_id>\d+)/$', views.albums, name='albums'),
    
    #New album
    url(r'^add_album/$', views.add_album, name='add_album'),
    
    url(r'^add_song/(?P<album_id>\d+)/$', views.add_song, name='add_song'),
    
]

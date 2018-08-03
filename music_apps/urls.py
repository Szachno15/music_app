
from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    
    #Shows all albums
    url(r'^detail/$', views.detail, name='detail'),
    
    #Individual pages for Album
    url(r'^detail/(?P<album_id>\d+)/$', views.albums, name='albums'),
    
    url(r'^add_album/$', views.add_album, name='add_album'),
    
    url(r'^add_song/(?P<album_id>\d+)/$', views.add_song, name='add_song'),
    
    url(r'^edit_song/(?P<song_id>\d+)/$', views.edit_song, name='edit_song'),
    
]

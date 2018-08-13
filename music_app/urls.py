
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('music_apps.urls', namespace='music_apps')), 
    url(r'^users', include('user_app.urls', namespace='user_app')),
    
]

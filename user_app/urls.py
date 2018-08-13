
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login

from . import views
urlpatterns = [
   url(r'^login/$', login, {'template_name': 'user_app/login.html'},
		name='login'),
		
   url(r'^logout/$', views.logout_view, name='logout'),
   
   url(r'^register/$', views.register, name='register'),
   
]

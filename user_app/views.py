
from __future__ import unicode_literals
from django.shortcuts import render
from django.conf.urls import url
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm

def logout_view(request):

	logout(request)
	return HttpResponseRedirect(reverse('music_apps:index'))
	
def register(request):
	if request.method != 'POST':
		form = UserCreationForm()
	else:
		form = UserCreationForm(data=request.POST)
		new_user = form.save()
		user_authenticate = authenticate(username=new_user.username, 
			password = request.POST['password1'])
		login(request, user_authenticate)
		return HttpResponseRedirect(reverse('music_apps:index'))

	context = {'form': form }
	return render(request, 'user_app/register.html', context)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render

from .forms import AlbumForm, SongForm
from .models import Album, Song

def index(request):
	return render(request, 'music_apps/index.html') 
	
def detail(request):
	album = Album.objects.all()
	context = {'album':album}
	return render(request, 'music_apps/detail.html', context)
	
def albums(request, album_id):
	album = Album.objects.get(pk=album_id)
	song = album.song_set.order_by()
	context = {'album':album, 'song':song}
	return render(request, 'music_apps/album_id.html', context)
	
def add_album(request):
	#New song for a particular album
	if request.method != 'POST':
		form = AlbumForm() 
	else:
		form = AlbumForm(data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('music_apps:detail'))			
			
	context = {'form':form}
	return render(request, 'music_apps/add_album.html', context)
	
def add_song(request, album_id):
	album = Album.objects.get(pk=album_id) 
	if request.method != 'POST':
		form = SongForm()
	else:
		form = SongForm(data=request.POST)
		if form.is_valid():
			new_song = form.save(commit=False)
			new_song.album = album
			new_song.save()
			return HttpResponseRedirect(reverse('music_apps:albums', args=[album_id]))
		
	context = {'album':album, 'form':form}
	return render(request, 'music_apps/add_song.html', context)
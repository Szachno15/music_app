
from __future__ import unicode_literals
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import AlbumForm, SongForm
from .models import Album, Song

def index(request):
	return render(request, 'music_apps/index.html') 
	
@login_required	
def detail(request):
	album = Album.objects.filter(owner=request.user).order_by()
	context = {'album':album}
	return render(request, 'music_apps/detail.html', context)

@login_required
def albums(request, album_id):
	album = Album.objects.get(pk=album_id)
	if album.owner != request.user:
		raise 404
	song = album.song_set.order_by()
	context = {'album':album, 'song':song}
	return render(request, 'music_apps/album_id.html', context)

@login_required
def add_album(request):
	#New song for a particular album
	if request.method != 'POST':
		form = AlbumForm() 
	else:
		form = AlbumForm(data=request.POST)
		if form.is_valid():
			new_album = form.save(commit=False)
			new_album.owner = request.user
			new_album.save()
			return HttpResponseRedirect(reverse('music_apps:detail'))			
			
	context = {'form':form}
	return render(request, 'music_apps/add_album.html', context)
	
@login_required
def add_song(request, album_id):
	album = Album.objects.get(pk=album_id) 
	song = album.song_set.order_by()
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
	
@login_required
def edit_song(request, song_id):
	song = Song.objects.get(pk=song_id)
	album = song.album
	if album.owner != request.user:
		raise 404
	if request.method != 'POST':
		form = SongForm(instance=song)
	else:
		form = SongForm(data=request.POST, instance=song)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('music_apps:albums', args=[album.id]))
			
	context = {'form':form, 'album':album, 'song':song}
	return render(request, 'music_apps/edit_song.html', context)
	
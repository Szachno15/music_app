# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .models import Album, Song

def index(request):
	return render(request, 'music_apps/index.html') 
	
def detail(request):
	album = Album.objects.all()
	context = {'album':album}
	return render(request, 'music_apps/detail.html', context)
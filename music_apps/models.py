# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Album(models.Model):
	album = models.CharField(max_length=100)
	album_dp = models.TextField()
	artist = models.CharField(max_length=100)
	logo = models.FileField(max_length=100)
    
	def __str__(self):
		return self.album 
		

class Song(models.Model):
	album = models.ForeignKey(Album)
	song = models.CharField(max_length=100)
	song_url = models.CharField(max_length=150)
	
	def __str__(self):
		return self.song


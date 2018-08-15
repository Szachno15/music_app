# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Album(models.Model):
	album = models.CharField(max_length=100)
	album_dp = models.TextField()
	artist = models.CharField(max_length=100)
	logo = models.FileField(max_length=100)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
	def __str__(self):
		return self.album 
		

class Song(models.Model):
	album = models.ForeignKey(Album, on_delete=models.CASCADE)
	song = models.CharField(max_length=100)
	song_url = models.CharField(max_length=150, default='Paste URL here')
	
	def __str__(self):
		return self.song 


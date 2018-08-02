from .models import Album, Song
from django import forms

class AlbumForm(forms.ModelForm):
	class Meta:
		model = Album
		fields = ['artist', 'album']
		label = {'text':''}
		
class SongForm(forms.ModelForm):
	class Meta:	
		model = Song
		fields = ['song', 'song_url']
		label = {'text':''}
		widget = {'text': forms.Textarea(attrs={'cols':80})}
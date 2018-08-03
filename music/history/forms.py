from django import forms
from .models import Artist

class ArtistForm(forms.ModelForm):

  class Meta:
      model = Artist
      fields = ('artist_name', 'est_date')

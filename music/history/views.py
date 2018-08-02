from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Artist, Album


def index(request):
    artist_list = Artist.objects.order_by('-est_date')[:5]
    context = {'artist_list': artist_list}
    return render(request, 'history/index.html', context)

# gets the details of artist including their song
def artist(request, artist_id):
    print(artist_id)
    try:
        artist = Artist.objects.get(pk=artist_id)
    except Artist.DoesNotExist:
        raise Http404("Artist does not exist")
    return render(request, 'history/songs.html', {'artist': artist})

def song_view(request, artist_id, album_id):
    print(album_id)
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album Detail does not exist")
    return render(request, 'history/collection_list.html', {'album': album})
  



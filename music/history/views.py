from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.generic import ListView, TemplateView, FormView, DetailView, CreateView

from .models import Artist, Album
from .forms import ArtistForm


def index(request):
    artist_list = Artist.objects.order_by('-est_date')[:5]
    context = {'artist_list': artist_list}
    return render(request, 'history/index.html', context)

    def return_artist_form(self):
        return ArtistFormView

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


class ArtistFormView(FormView):
  template_name = 'history/artist_form.html'
  form_class = ArtistForm
  # NOTE! Be sure to put the slash in front of the url to route properly
  success_url = '/history/'

  def form_valid(self, form):
    # This method is called when valid form data has been POSTed.
    # It should return an HttpResponse.
    form.save()
    return super(ArtistFormView, self).form_valid(form)
  
  



from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Artist


def index(request):
    latest_question_list = Artist.objects.order_by('-est_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'history/index.html', context)

# gets the details of artist including their song
def artist(request, artist_id):
    try:
        question = Artist.objects.get(pk=artist_id)
    except Artist.DoesNotExist:
        raise Http404("Artist does not exist")
    return render(request, 'history/songs.html', {'question': question})



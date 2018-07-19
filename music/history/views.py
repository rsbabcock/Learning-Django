from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Artist


def index(request):
    latest_question_list = Artist.objects.order_by('-est_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'history/index.html', context)

# Leave the rest of the views (detail, results, vote) unchanged
def artist(request, artist_id):
    try:
        question = Artist.objects.get(pk=artist_id)
    except Artist.DoesNotExist:
        raise Http404("Artist does not exist")
    return render(request, 'history/songs.html', {'question': question})

def songs(request, artist_id):
    try:
        question = Artist.objects.get(pk=question_id)
    except Artist.DoesNotExist:
        raise Http404("Artist does not exist")
    return render(request, 'history/songs.html', {'question': question})
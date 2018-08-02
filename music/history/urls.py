from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:artist_id>/', views.artist, name='artist'),
    
    path('<int:artist_id>/albums/', views.song_view, name='song_view')
    # ex: /polls/5/results/
    # path('<int:artist_id>/song/', views.songs, name='songs'),
]
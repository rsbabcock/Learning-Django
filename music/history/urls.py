from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:artist_id>/', views.artist, name='artist'),
    # ex: /polls/5/results/
    # path('<int:artist_id>/song/', views.songs, name='songs'),
]
from django.db import models


class Artist(models.Model):
    artist_name = models.CharField(max_length=200)
    est_date = models.IntegerField('date established')
    def __str__(self):
        return self.artist_name


class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    song_text = models.CharField(max_length=200)
    song_length = models.IntegerField(default=0)
    def __str__(self):
        return self.song_text
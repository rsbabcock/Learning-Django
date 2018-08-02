from django.db import models


class Artist(models.Model):
    artist_name = models.CharField(max_length=200)
    est_date = models.IntegerField('date established')
    def __str__(self):
        return self.artist_name


class Song(models.Model):
    album = models.ForeignKey('Album', on_delete=models.CASCADE)
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE)
    song_title = models.CharField(max_length=200)
    song_length = models.IntegerField(default=0)
    def __str__(self):
        return self.song_text

class Album(models.Model):
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE)
    album_name = models.CharField(max_length=200)
    album_length = models.IntegerField(default=0)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    def __str__(self):
        return self.album_name

class Genre(models.Model):
    genre_name = models.CharField(max_length=200)
    def __str__(self):
        return self.genre_name

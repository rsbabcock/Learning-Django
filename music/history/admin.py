from django.contrib import admin

from .models import Song, Artist


class SongInline(admin.StackedInline):
    model = Song


class ArtistAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['artist_name']}),
        ('Date information', {'fields': ['est_date'], 'classes': ['collapse']}),
    ]
    inlines = [SongInline]

admin.site.register(Artist, ArtistAdmin)
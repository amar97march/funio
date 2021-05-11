''' Serializer for Audio Files'''
from django.contrib import admin
from audio.models import *


class SongAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration', 'uploaded_time',)
    search_fields = ('name', 'duration', 'uploaded_time',)


admin.site.register(Song, SongAdmin)


class PodcastAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration', 'uploaded_time',
                    'host', 'participants',)
    search_fields = ('name', 'duration', 'uploaded_time',
                     'host', 'participants',)


admin.site.register(Podcast, PodcastAdmin)


class AudiobookAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration', 'uploaded_time',
                    'author', 'narrator',)
    search_fields = ('title', 'duration', 'uploaded_time',
                     'author', 'narrator',)


admin.site.register(Audiobook, AudiobookAdmin)

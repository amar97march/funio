from rest_framework import serializers
from .models import Song, Podcast, Audiobook
from django.utils.timezone import now


class SongSerializer(serializers.Serializer):
    class Meta:
        model = Song
        fields = ('id', 'name', 'duration', 'uploaded_time')
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    duration = serializers.IntegerField()
    uploaded_time = serializers.DateTimeField(default=now)

    def create(self, validated_data):
        song = Song.objects.create(**validated_data)
        return song

    def update(self, instance, validated_data):
        # perform instance update
        instance.name = validated_data.get('name', instance.name)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.save()
        return instance


class PodcastSerializer(serializers.Serializer):
    class Meta:
        model = Podcast
        fields = ('id', 'name', 'duration', 'host',
                  'participants', 'uploaded_time')
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    duration = serializers.IntegerField()
    host = serializers.CharField(max_length=100)
    participants = serializers.ListField(
        child=serializers.CharField(max_length=100), max_length=10)
    uploaded_time = serializers.DateTimeField(default=now)

    def create(self, validated_data):
        podcast = Podcast.objects.create(**validated_data)

        return podcast

    def update(self, instance, validated_data):
        # perform instance update
        instance.name = validated_data.get('name', instance.name)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.host = validated_data.get('host', instance.host)
        instance.participants = validated_data.get(
            'participants', instance.participants)

        instance.save()
        return instance


class AudiobookSerializer(serializers.Serializer):
    class Meta:
        model = Audiobook
        fields = ('id', 'title', 'duration', 'host', 'uploaded_time')
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    duration = serializers.IntegerField()
    author = serializers.CharField(max_length=100)
    narrator = serializers.CharField(max_length=100)
    uploaded_time = serializers.DateTimeField(default=now)

    def create(self, validated_data):
        audiobook = Audiobook.objects.create(**validated_data)

        return audiobook

    def update(self, instance, validated_data):
        # perform instance update
        instance.title = validated_data.get('title', instance.title)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.author = validated_data.get('author', instance.author)
        instance.narrator = validated_data.get('narrator', instance.narrator)

        instance.save()
        return instance

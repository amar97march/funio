from django.test import TestCase, Client
import json
from django.urls import reverse
from rest_framework import status
from .models import Song, Audiobook, Podcast

client = Client()


class CreateSong(TestCase):
    """ Test module for inserting a new song """
    song_id = 0

    def setUp(self):
        self.song = Song.objects.create(
            name='Song1', duration=1)
        self.valid_payload = {
            "audioFileType": "song",
            "audioFileMetadata": {
                "name": "song test",
                "duration": 120
            }
        }
        self.invalid_payload = {
            "audioFileType": "song",
            "audioFileMetadata": {
                "name": "song test",
                "durations": 120
            }
        }

        self.invalid_extra_long_name = {
            "audioFileType": "song",
            "audioFileMetadata": {
                "name": "song testsong testsong testsong testsong testsong testsong testsong testsong testsong testsong testsong testsong testsong testsong testsong testsong testsong testsong testsong testsong testsong testsong testsong testsong testsong testsong testsong testsong testsong testsong testsong testsong testsong testsong testsong testsong test",
                "durations": 120
            }
        }
    # Create Song

    def test_create_valid_song(self):
        response = client.post(
            reverse('files_api'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.song_id = response.json()["data"]["id"]
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_invalid_song(self):
        response = client.post(
            reverse('files_api'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_invalid_song_extra_long_name(self):
        response = client.post(
            reverse('files_api'),
            data=json.dumps(self.invalid_extra_long_name),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # Update Song
    def test_update_valid_song(self):
        response = client.put(
            reverse('files_instance_api', kwargs={
                    'audioFileType': "song", "audioFileId": self.song.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_invalid_song(self):
        response = client.put(
            reverse('files_instance_api',
                    kwargs={
                        'audioFileType': "song", "audioFileId": self.song.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # Fetch Song
    def test_get_list(self):
        response = client.get(
            reverse('files_list', kwargs={'audioFileType': "song"})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_instance(self):
        response = client.get(
            reverse('files_instance_api', kwargs={
                    'audioFileType': "song", "audioFileId": self.song.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Delete Song
    def test_delete_instance(self):
        response = client.get(
            reverse('files_instance_api', kwargs={
                    'audioFileType': "song", "audioFileId": self.song.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CreatePodcast(TestCase):
    """ Test module for inserting a new podcast """

    def setUp(self):
        self.podcast = Podcast.objects.create(
            name='Podcast1', duration=1, host="test", participants=["abc"])
        self.valid_payload = {
            "audioFileType": "podcast",
            "audioFileMetadata": {
                "name": "podcast test",
                "duration": 333320,
                "host": "test",
                "participants": ["abc"]
            }
        }
        self.invalid_payload = {
            "audioFileType": "podcast",
            "audioFileMetadata": {
                "name": "song testsong testsong testsong testsong testsong testsong testsong testsong testsong testsong testsong testsong test",
                "duration": 333320,
                "host": "test",
                "participants": ["abc"]
            }
        }

        self.invalid_participants_length = {
            "audioFileType": "podcast",
            "audioFileMetadata": {
                "name": "song test",
                "duration": 333320,
                "host": "test",
                "participants": ["abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc"]
            }
        }

    #  Create Podcast
    def test_create_valid_podcast(self):
        response = client.post(
            reverse('files_api'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.podcast_id = response.json()["data"]["id"]
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_invalid_podcast(self):
        response = client.post(
            reverse('files_api'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_invalid_participants_length(self):
        response = client.post(
            reverse('files_api'),
            data=json.dumps(self.invalid_participants_length),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # Update Podcast
    def test_update_valid_podcast(self):
        response = client.put(
            reverse('files_instance_api', kwargs={
                    'audioFileType': "podcast", "audioFileId": self.podcast.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_invalid_podcast(self):
        response = client.put(
            reverse('files_instance_api',
                    kwargs={
                        'audioFileType': "podcast", "audioFileId": self.podcast.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # Get Podcast
    def test_get_list(self):
        response = client.get(
            reverse('files_list', kwargs={'audioFileType': "podcast"})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_instance(self):
        response = client.get(
            reverse('files_instance_api', kwargs={
                    'audioFileType': "podcast", "audioFileId": self.podcast.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Delete Podcast
    def test_delete_instance(self):
        response = client.get(
            reverse('files_instance_api', kwargs={
                    'audioFileType': "podcast", "audioFileId": self.podcast.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CreateAudiobook(TestCase):
    """ Test module for inserting a new audiobook """

    def setUp(self):
        self.audiobook = Audiobook.objects.create(
            title='Podcast1', duration=1, author="test", narrator="abc")
        self.valid_payload = {
            "audioFileType": "audiobook",
            "audioFileMetadata": {
                "title": "song test",
                "duration": 30,
                "author": "test",
                "narrator": "abc"
            }
        }
        self.invalid_payload = {
            "audioFileType": "audiobook",
            "audioFileMetadata": {
                "name": "song test",
                "duration": 20,
                "author": "test",
                "narrator": "abc"
            }
        }

        self.invalid_blank_author = {
            "audioFileType": "audiobook",
            "audioFileMetadata": {
                "title": "song test",
                "duration": 50,
                "author": "",
                "narrator": "abc"
            }
        }

    #  Create Audiobook
    def test_create_valid_audiobook(self):
        response = client.post(
            reverse('files_api'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.audiobook_id = response.json()["data"]["id"]
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_invalid_audiobook(self):
        response = client.post(
            reverse('files_api'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_invalid_blank_author(self):
        response = client.post(
            reverse('files_api'),
            data=json.dumps(self.invalid_blank_author),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # Update Audiobook
    def test_update_valid_audiobook(self):
        response = client.put(
            reverse('files_instance_api', kwargs={
                    'audioFileType': "audiobook", "audioFileId": self.audiobook.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_invalid_audiobook(self):
        response = client.put(
            reverse('files_instance_api',
                    kwargs={
                        'audioFileType': "audiobook", "audioFileId": self.audiobook.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # Get Audiobook
    def test_get_list(self):
        response = client.get(
            reverse('files_list', kwargs={'audioFileType': "audiobook"})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_instance(self):
        response = client.get(
            reverse('files_instance_api', kwargs={
                    'audioFileType': "audiobook", "audioFileId": self.audiobook.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Delete Audiobook
    def test_delete_instance(self):
        response = client.get(
            reverse('files_instance_api', kwargs={
                    'audioFileType': "audiobook", "audioFileId": self.audiobook.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

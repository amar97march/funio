''' Views for Audio Urls '''
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from .models import Song, Audiobook, Podcast
from django.forms.models import model_to_dict
from .serializers import SongSerializer, PodcastSerializer, AudiobookSerializer


class FileAPI(APIView):

    def post(self, request):
        ''' Create Audio file Method '''
        audioFileType = request.data.get('audioFileType', None)
        data = request.data.get('audioFileMetadata', {})

        if audioFileType not in ["song", "podcast", "audiobook"]:
            return JsonResponse({'error': 'invalid upload file type {}.'.format(audioFileType)}, status=400)
        else:
            try:

                if audioFileType == "song":
                    ser_obj = SongSerializer(data=data)
                    if not ser_obj.is_valid():
                        return JsonResponse({"error": ser_obj.errors}, status=400)
                elif audioFileType == "podcast":

                    ser_obj = PodcastSerializer(data=data)
                    if not ser_obj.is_valid():
                        return JsonResponse({"error": ser_obj.errors}, status=400)
                else:
                    ser_obj = AudiobookSerializer(data=data)
                    if not ser_obj.is_valid():
                        return JsonResponse({"error": ser_obj.errors}, status=400)
                ser_obj.save()
                return JsonResponse({'status': '{} uploaded successfully.'.format(audioFileType), "data": ser_obj.data}, status=200)
            except Exception as e:
                return JsonResponse({"error": str(e)}, status=400)


class FileListAPI(APIView):

    def get(self, request, audioFileType):
        ''' Get Audio file list Method '''
        if audioFileType not in ["song", "podcast", "audiobook"]:
            return JsonResponse({'error': 'invalid file type {}.'.format(audioFileType)}, status=400)
        else:
            try:
                if audioFileType == "song":
                    objs = Song.objects.all()
                    data = SongSerializer(objs, many=True)
                elif audioFileType == "podcast":
                    objs = Podcast.objects.all()
                    data = PodcastSerializer(objs, many=True)
                else:
                    objs = Audiobook.objects.all()
                    data = AudiobookSerializer(objs, many=True)
                return JsonResponse({'data': data.data}, status=200)
            except:
                return JsonResponse({"error": "invalid id"}, status=400)


class FileUpdateAPI(APIView):

    def get(self, request, audioFileType, audioFileId):
        ''' Get Audio file Method '''
        if audioFileType not in ["song", "podcast", "audiobook"]:
            return JsonResponse({'error': 'invalid file type {}.'.format(audioFileType)}, status=400)
        else:
            try:
                if audioFileType == "song":
                    obj = Song.objects.get(id=int(audioFileId))
                elif audioFileType == "podcast":
                    obj = Podcast.objects.get(id=(audioFileId))
                else:
                    obj = Audiobook.objects.get(id=int(audioFileId))

                return JsonResponse({'data': model_to_dict(obj)}, status=200)
            except:
                return JsonResponse({"error": "invalid id"}, status=400)

    def put(self, request, audioFileType, audioFileId):
        ''' Update Audio file Method '''
        data = request.data.get('audioFileMetadata', {})
        if audioFileType not in ["song", "podcast", "audiobook"]:
            return JsonResponse({'error': 'invalid file type {}.'.format(audioFileType)}, status=400)
        else:
            try:
                if audioFileType == "song":
                    obj = Song.objects.get(id=int(audioFileId))
                    ser_obj = SongSerializer(obj, data)
                    if not ser_obj.is_valid():
                        return JsonResponse({"error": ser_obj.errors}, status=400)
                elif audioFileType == "podcast":
                    obj = Podcast.objects.get(id=(audioFileId))
                    ser_obj = PodcastSerializer(obj, data)
                    if not ser_obj.is_valid():
                        return JsonResponse({"error": ser_obj.errors}, status=400)
                else:
                    obj = Audiobook.objects.get(id=int(audioFileId))
                    ser_obj = AudiobookSerializer(obj, data)
                    if not ser_obj.is_valid():
                        return JsonResponse({"error": ser_obj.errors}, status=400)
                ser_obj.save()

                return JsonResponse({'status': "Updated"}, status=200)
            except:
                return JsonResponse({"error": "invalid id"}, status=400)

    def delete(self, request, audioFileType, audioFileId):
        ''' Delete Audio file Method '''
        if audioFileType not in ["song", "podcast", "audiobook"]:
            return JsonResponse({'error': 'invalid file type {}.'.format(audioFileType)}, status=400)
        else:
            try:
                if audioFileType == "song":
                    obj = Song.objects.get(id=int(audioFileId))
                elif audioFileType == "podcast":
                    obj = Podcast.objects.get(id=(audioFileId))
                else:
                    obj = Audiobook.objects.get(id=int(audioFileId))
                obj.delete()

                return JsonResponse({'status': "deleted"}, status=200)
            except:
                return JsonResponse({"error": "invalid id"}, status=400)

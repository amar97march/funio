''' Urls for audio files '''
from django.conf.urls import url
from audio.views import *


urlpatterns = [
    url(r'^(?P<audioFileType>\w+)/(?P<audioFileId>\w+)/',
        FileUpdateAPI.as_view(), name='files_instance_api'),
    url(r'^(?P<audioFileType>\w+)/',
        FileListAPI.as_view(), name='files_list'),
    url(r'^', FileAPI.as_view(), name='files_api'),
]

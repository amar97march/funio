'''Models for Audio Urls '''
from django.db import models
from datetime import date
from django.conf import settings
import os
from django_mysql.models import ListCharField
from django.utils.timezone import now


class Song(models.Model):
    '''Model for Song
    '''
    name = models.CharField(max_length=100)
    duration = models.IntegerField(null=False, blank=False)
    uploaded_time = models.DateTimeField(default=now)


class Podcast(models.Model):
    '''Model for Podcast
    '''
    name = models.CharField(max_length=100)
    duration = models.IntegerField(null=False, blank=False)
    host = models.CharField(max_length=100, null=False, blank=False)
    uploaded_time = models.DateTimeField(default=now)
    participants = ListCharField(
        base_field=models.CharField(max_length=100),
        size=10,
        max_length=1009
    )


class Audiobook(models.Model):
    '''Model for Audiobook
    '''
    title = models.CharField(max_length=100, null=False, blank=False)
    author = models.CharField(max_length=100, null=False, blank=False)
    narrator = models.CharField(max_length=100, null=False, blank=False)
    duration = models.IntegerField(null=False, blank=False)
    uploaded_time = models.DateTimeField(default=now)

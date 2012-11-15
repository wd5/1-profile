# -*- coding:utf-8 -*-
from django.db import models
from google.appengine.ext import db
from image_storage.models import Image

class Profile(models.Model):
    first_name = models.CharField(max_length=256, null=False)
    last_name = models.CharField(max_length=256, null=False)
    email = models.EmailField(max_length=256, null=False)
    website = models.URLField(max_length=256, null=False)
    note = models.TextField()
    active = models.BooleanField(default=False)
    avatar = models.ForeignKey(Image, null=True)

def get_profile():
    profile = Profile.objects.filter(active=True)
    if profile.count():
        profile = profile[0]
    else:
        profile = Profile(
            first_name='Alex',
            last_name='Barauskas',
            email='barauskasalex@gmail.com',
            website='http://barauskasalex.appspot.com',
            active=True,
            note=u"Немного о себе. Я закончил Белорусский Государственный Университет по специальности математик-системный аналитик. На данный момент основной моей работой и основным хобби является web-разработка на Python/Django. Собственно на чем и реализована данная визитка.",
            )
        profile.save()
    return profile



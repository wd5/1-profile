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

    def get_contacts(self, t=None):
        if t is None:
            return self.contact_set.filter()
        return self.contact_set.filter(contact_type=t)

    def get_emails(self):
        qs = self.get_contacts(t='e')
        if qs.count() == 0:
            Contact(contact_type='e', contact='barauskasalex@gmail.com',
                    profile=self).save()
            return self.get_contacts(t='e')
        return qs

    def get_social(self):
        return self.get_contacts(t='n')

    def get_websites(self):
        return self.get_contacts(t='w')

    def get_messangers(self):
        return self.get_contacts(t='m')

    def get_other(self):
        return self.get_contacts(t='o')

    def get_skype(self):
        return self.get_contacts(t='s')



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


class Contact(models.Model):
    profile = models.ForeignKey(Profile, null=True)
    contact_type = models.CharField(max_length=1, null=False,
                                    choices=(('e', 'email'),
                                             ('n', 'social network'),
                                             ('w', 'websites'),
                                             ('s', 'skype'),
                                             ('m', 'messengers'),
                                             ('o', 'other'),
                                             )
                                    )
    title = models.CharField(max_length=32, null=True)
    contact = models.CharField(max_length=128, null=True)

    def __unicode__(self):
        return self.contact

#class 


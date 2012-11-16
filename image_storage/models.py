# -*- coding:utf-8 -*-
from django.db import models
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from google.appengine.ext import db
from django.conf import settings

class ImageBlob(db.Model):
    img = db.BlobProperty()

class Image(models.Model):
    image_id = models.PositiveIntegerField(_('Blog image ID'))
    name = models.CharField('Name', max_length=64)
    tag = models.CharField('Tag', max_length=32)
    active = models.BooleanField(default=False)

    def get_url(self):
        return reverse('get_img',kwargs={'img_id':self.id})

    def __unicode__(self):
        return self.get_url()

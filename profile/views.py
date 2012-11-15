# -*- coding:utf-8 -*-
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from models import get_profile


def index(request):
    return render_to_response('home.html',
                              {'profile': get_profile()},
                              context_instance=RequestContext(request))

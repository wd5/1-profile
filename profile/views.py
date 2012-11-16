# -*- coding:utf-8 -*-
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from models import get_profile

def index(request, template_name="home.html"):
    return render_to_response(template_name,
                              {'profile': get_profile()},
                              context_instance=RequestContext(request))


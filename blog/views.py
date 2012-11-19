# -*- coding:utf-8 -*-
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from models import Post
from forms import PostForm

from decorators import check_user

def index(request, tag=None):
    last_posts = Post.objects.filter(active=True).order_by('-created')[:3]
    return render_to_response('blog/index.html',
                              {'posts':last_posts},
                              context_instance=RequestContext(request))

def create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PostForm()
    return render_to_response('blog/edit.html',
                              {'form':form},
                              context_instance=RequestContext(request))
    

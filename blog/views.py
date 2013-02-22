# -*- coding:utf-8 -*-
from django.conf import settings
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from models import Post
from forms import PostForm, CommentForm

from decorators import check_user
from utils import get_user_name
from captcha import CaptchasDotNet
from random import random


def index(request, tag=None):
    tags = request.GET.getlist('tag')
    if tags:
        last_posts = Post.objects.filter(active=True,
                                         tag__in=tags).order_by('-created')[:10]
    else:
        last_posts = Post.objects.filter(active=True).order_by('-created')[:3]
    return render_to_response('blog/index.html',
                              {'posts': last_posts,
                               },
                              context_instance=RequestContext(request))


def post_view(request, post_id):
    post = get_object_or_404(Post,id=post_id)
    if not post.active:
        return HttpResponseNotFound()
    
    other_posts = Post.objects.filter(tag=post.tag).exclude(id=post.id)[:10]

    captcha = CaptchasDotNet(client = 'barauskas',secret   = 'K1Qurc2oCY09sJA63cpseGEz3zOpwzDeZeR6YNvf')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            if captcha.verify(form.cleaned_data['captcha'],request.session.get('rand','')):
                form.instance.post = post
                comment = form.save()
                #comment.post = post
                #comment.save()
                form = CommentForm(initial={'author':get_user_name()})
            else:
                form.errors['captcha']=['Captcha is unvalid!']
    else:
        form = CommentForm(initial={'author':get_user_name()})
    rand = str(int(random()*1000000))
    request.session['rand']=rand
    return render_to_response('blog/view.html',
                              {'post': post,
                               'other_posts': other_posts,
                               'form': form,
                               'captcha':captcha.image_url(rand)
                               },
                              context_instance=RequestContext(request))    


@check_user
def admin(request):
    return render_to_response('blog/admin.html',
                              {'posts': Post.objects.all()},
                              context_instance=RequestContext(request))
    

@check_user
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


@check_user
def edit(request,post_id):
    post = get_object_or_404(Post,id=post_id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
    else:
        form = PostForm(instance=post)
    return render_to_response('blog/edit.html',
                              {'form':form},
                              context_instance=RequestContext(request))
    

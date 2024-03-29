# -*- coding:utf-8 -*-
from django.conf import settings
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponseNotFound

from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from profile.models import get_profile, Work
from profile.forms import EditProfile, FormWork
from image_storage.views import _save_image

from decorators import check_user


@check_user
def edit_profile(request):
    profile = get_profile()
    if request.method == "POST":
        form = EditProfile(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            image = _save_image(request)
            if image:
                form.instance.avatar = image[0]
                form.instance.save()
    else:
        form = EditProfile(instance=profile)
    return render_to_response('edit/profile.html',
                              {'profile': get_profile(),
                               'form': form},
                              context_instance=RequestContext(request))


@check_user
def edit_work(request, work_id=None):
    profile = get_profile()
    forms = map(lambda x: FormWork(instance=x, prefix='%s' % x.id),
                profile.work_set.all())
    if request.method == "POST":
        work = None
        if work_id is not None:
            work = Work.objects.filter(id=work_id)
        if work:
            form = FormWork(request.POST, instance=work[0],
                            prefix='%s' % work[0].id)
        else:
            form = FormWork(request.POST)
        if form.is_valid():
            form.save()
            if not work:
                forms.append(form)
            else:
                return HttpResponseRedirect('.')
            form = FormWork()
    else:
        form = FormWork()
    forms.append(form)
    return render_to_response('edit/work.html',
                              {'profile': get_profile(),
                               'forms': forms,
                               },
                              context_instance=RequestContext(request))

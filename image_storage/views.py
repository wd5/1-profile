from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render_to_response

from google.appengine.ext import db

from image_storage.models import ImageBlob, Image

def _save_image(request):
    res = []
    for file_name in request.FILES.keys():
        img = request.FILES[file_name]
        name = img.name
        tag = request.POST.get('tag','')
        storeimage = ImageBlob()
        storeimage.img = db.Blob(img.read())
        key = storeimage.put()

        IMG = Image(image_id=key.id(),
                    tag=tag,
                    name=name,
                    )
        IMG.save()
        res.append(IMG)
    return res

def get_image(request,img_id):
    img = get_object_or_404(Image,id=img_id)
    Q = ImageBlob.get_by_id(img.image_id, parent=None)
    if Q:
        img=Q.img
    else:
        return HttpResponseNotFound()
    response = HttpResponse(img)
    response['Content-Type'] = 'image/png'
    return response

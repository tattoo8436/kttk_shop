import json
from django.shortcuts import render
# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect

from .models import ImageModel
from django.views.decorators.csrf import csrf_exempt
from .models import ImageForm
# Create your views here.
@csrf_exempt
def img(request):
    resp = {}
    resp['status'] = 'Success'
    resp['status_code'] = '200'
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            img = ImageModel(img = request.FILES['img'], productId = request.POST.get('productId'))
            img.save()
    if request.method == 'GET':
        x = list(ImageModel.objects.filter(productId = request.GET.get('productId')))
        if x:
            return HttpResponse(x[0].img, content_type='image')
    return HttpResponse(json.dumps(resp), content_type='application/json')



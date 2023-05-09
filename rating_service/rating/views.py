# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Rating as cmt
# This function is for fetching the user data.
import requests

@csrf_exempt
def useRating(request):
    resp = {}
    if request.method == 'POST':
        body = json.loads(request.body)
        uname = body.get("username")
        productId = body.get("productId")
        rating = body.get("rating")
        if not rating or rating < 0 or rating > 5:
            resp['status'] = 'Fail'
            resp['status_code'] = '400'
            resp['message'] = 'Invalid Rating'
            return HttpResponse(json.dumps(resp), content_type='application/json')

        url = 'http://127.0.0.1:8001/product/?productId='+str(productId)
        response = requests.get(url)
        url2 = 'http://127.0.0.1:8000/info/'
        js = {"username": uname}
        response2 = requests.post(url2, json=js)
        try:
            print(response2)
            val1 = json.loads(response.content.decode('utf-8'))['data']
            val2 = json.loads(response2.content.decode('utf-8'))['data']
        except:
            resp['status'] = 'Fail'
            resp['status_code'] = '400'
            resp['message'] = 'Invalid Product Or Username'
        if uname and productId and rating:
            commentData = cmt(
                username=uname, productId=productId, rating=rating)
            x = commentData.save()
            print('this')
            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['data'] = x
    if request.method == 'GET':
        productId = request.GET.get("productId")
        if productId:
            resp['data'] = list(cmt.objects.filter(productId = productId).values())
            resp['status'] = 'Success'
            resp['status_code'] = '200'
    return HttpResponse(json.dumps(resp), content_type='application/json')

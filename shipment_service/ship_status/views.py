# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from .models import ShipmentModel 
import requests

@csrf_exempt
def changeShip(request):
    resp = {}
    resp['status'] = 'ERROR'
    resp['status_code'] = '400'
    body = json.loads(request.body)
    uname = body.get("username")
    id = body.get("shipmentId")
    status = body.get("status")
    try:
        x = ShipmentModel.objects.filter(username=uname, id=id)
        x.update(status=status)
        resp['status'] = 'Success'
        resp['status_code'] = '200'
    except:
        resp['message'] = 'Not found'
    return HttpResponse(json.dumps(resp), content_type='application/json')

@csrf_exempt
def useShipment(request):
    resp = {}
    resp['status'] = 'ERROR'
    resp['status_code'] = '400'
    if request.method == 'POST':
        body = json.loads(request.body)
        uname = body.get("username")
        checkoutId = body.get("checkoutId")
        mobile = body.get("mobile")
        address = body.get("address")
        try:
            url2 = 'http://127.0.0.1:8004/checkPay/'
            js = {"username": uname, "checkoutId": checkoutId}
            response2 = requests.post(url2, json=js)
            val2 = json.loads(response2.content.decode('utf-8'))['data']
            ShipmentModel(username=uname, checkoutId=checkoutId,
                        address=address, mobile=mobile,
                        status='Preparing').save()
            url2 = 'http://127.0.0.1:8004/paid/'
            js = {"username": uname, "checkoutId": checkoutId}
            response2 = requests.post(url2, json=js)
            resp['status'] = 'Success'
            resp['status_code'] = '200'
            return HttpResponse(json.dumps(resp), content_type='application/json')
        except:
            resp['message'] = 'Not found'
    if request.method == 'GET':
        username = request.GET.get("username")
        if username:
            resp['data'] = list(ShipmentModel.objects.filter(
                username=username).values())
            resp['status'] = 'Success'
            resp['status_code'] = '200'
    if request.method == 'DELETE':
        id = request.GET.get("id")
        if id:
            try:
                ca = ShipmentModel.objects.get(id=id)
                if ca:
                    ca.delete()
                    resp['status'] = 'Success'
                    resp['status_code'] = '200'
            except:
                resp['data'] = 'Not found'
# If a user is not found then it give failed as response.
    return HttpResponse(json.dumps(resp), content_type='application/json')




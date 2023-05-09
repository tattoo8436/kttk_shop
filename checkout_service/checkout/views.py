import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import requests

from .models import CheckoutModel


# Create your views here.
@csrf_exempt
def check(request):
    resp = {}
    resp['status'] = 'ERROR'
    resp['status_code'] = '400'
    body = json.loads(request.body)
    uname = body.get("username")
    id = body.get("checkoutId")
    try:
        x = CheckoutModel.objects.filter(username=uname, id=id).values().first()
        x.get('id')
        resp['data'] = x
        resp['status'] = 'Success'
        resp['status_code'] = '200'
    except:
        resp['message'] = 'Not found'
    return HttpResponse(json.dumps(resp), content_type='application/json')

@csrf_exempt
def paid(request):
    resp = {}
    resp['status'] = 'ERROR'
    resp['status_code'] = '400'
    body = json.loads(request.body)
    uname = body.get("username")
    id = body.get("checkoutId")
    try:
        x = CheckoutModel.objects.filter(username=uname, id=id)
        x.update(isPay=True)
        resp['status'] = 'Success'
        resp['status_code'] = '200'
    except:
        resp['message'] = 'Not found'
    return HttpResponse(json.dumps(resp), content_type='application/json')

@csrf_exempt
def useCheckout(request):
    resp = {}
    resp['status'] = 'ERROR'
    resp['status_code'] = '400'
    if request.method == 'POST':
        body = json.loads(request.body)
        uname = body.get("username")
        cartIds = body.get("cartIds")
        x = 0
        for cid in cartIds:
            try:
                url2 = 'http://127.0.0.1:8003/cart/check/'
                js = {"username": uname, "cartId": cid}
                response2 = requests.post(url2, json=js)
                val2 = json.loads(response2.content.decode('utf-8'))['data']
                x = x + val2
            except:
                resp['message'] = 'Not found at cartId = ' + str(cid)
                return HttpResponse(json.dumps(resp), content_type='application/json')

        CheckoutModel(username=uname, cartIds=cartIds, totalPrice = x).save()
        for cid in cartIds:
            url2 = 'http://127.0.0.1:8003/cart/checkout/'
            js = {"username": uname, "cartId": cid}
            response2 = requests.post(url2, json=js)
        resp['status'] = 'Success'
        resp['status_code'] = '200'
    if request.method == 'GET':
        username = request.GET.get("username")
        if username:
            resp['data'] = list(CheckoutModel.objects.filter(
                username=username).values())
            resp['status'] = 'Success'
            resp['status_code'] = '200'
    if request.method == 'DELETE':
        id = request.GET.get("id")
        if id:
            try:
                ca = CheckoutModel.objects.get(id=id)
                if ca:
                    ca.delete()
                    resp['status'] = 'Success'
                    resp['status_code'] = '200'
            except:
                resp['data'] = 'Not found'
# If a user is not found then it give failed as response.
    return HttpResponse(json.dumps(resp), content_type='application/json')

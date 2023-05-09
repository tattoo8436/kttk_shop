import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import requests

from .models import OrderModel

@csrf_exempt
def useOrder(request):
    resp = {}
    resp['status'] = 'ERROR'
    resp['status_code'] = '400'
    if request.method == 'POST':
        body = json.loads(request.body)
        uname = body.get("username")
        productId = body.get("productId")
        quantity = body.get("quantity")

        url = 'http://127.0.0.1:8001/product/?productId='+str(productId)
        response = requests.get(url)
        url2 = 'http://127.0.0.1:8000/info/'
        js = {"username": uname}
        response2 = requests.post(url2, json=js)
        val1 = 0
        try:
            print(response2)
            val1 = json.loads(response.content.decode('utf-8'))['data']
            print(val1)
            val2 = json.loads(response2.content.decode('utf-8'))['data']
        except:
            resp['status'] = 'Fail'
            resp['status_code'] = '400'
            resp['message'] = 'Invalid Product Or Username'
        if quantity and quantity <= val1.get('quantity'):
            c = OrderModel(
                username=uname, productId=productId, quantity=quantity, price=val1.get('price'))
            x = c.save()
            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['data'] = x
        else:
            resp['status'] = 'Fail'
            resp['status_code'] = '400'
            resp['message'] = 'Not enough: ' + str(quantity) + ' > ' + str(val1.get('quantity'))
    if request.method == 'GET':
        username = request.GET.get("username")
        if username:
            resp['data'] = list(OrderModel.objects.filter(
                username=username).values())
            resp['status'] = 'Success'
            resp['status_code'] = '200'
    if request.method == 'DELETE':
        id = request.GET.get("id")
        if id:
            try:
                ca = OrderModel.objects.get(id=id)
                if ca:
                    ca.delete()
                    resp['status'] = 'Success'
                    resp['status_code'] = '200'
            except:
                resp['data'] = 'Not found'
    return HttpResponse(json.dumps(resp), content_type='application/json')

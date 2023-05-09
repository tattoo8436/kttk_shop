import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import requests

from .models import PaymentModel

@csrf_exempt
def pay(request):
    resp = {}
    resp['status'] = 'ERROR'
    resp['status_code'] = '400'
    body = json.loads(request.body)
    uname = body.get("username")
    id = body.get("paymentId")
    x = PaymentModel.objects.filter(username=uname, id=id, status='unpaid').first()
    if x:
        x.status = 'paid'
        x.save()
        resp['status'] = 'Success'
        resp['status_code'] = '200'
    else:
        resp['message'] = 'Not found'
    return HttpResponse(json.dumps(resp), content_type='application/json')

@csrf_exempt
def usePayment(request):
    resp = {}
    resp['status'] = 'ERROR'
    resp['status_code'] = '400'
    if request.method == 'POST':
        body = json.loads(request.body)
        uname = body.get("username")
        checkoutId = body.get("checkoutId")
        type = body.get("type")
        mobile = body.get("mobile")
        try:
            url2 = 'http://127.0.0.1:8004/checkPay/'
            js = {"username": uname, "checkoutId": checkoutId}
            response2 = requests.post(url2, json=js)
            val2 = json.loads(response2.content.decode('utf-8'))['data']
            if val2.get('isPay') == False:
                PaymentModel(username=uname, checkoutId=checkoutId,
                            totalPrice=val2.get('totalPrice'),
                            type=type, mobile=mobile,
                            status='unpaid').save()
                url2 = 'http://127.0.0.1:8004/paid/'
                js = {"username": uname, "checkoutId": checkoutId}
                response2 = requests.post(url2, json=js)
                resp['status'] = 'Success'
                resp['status_code'] = '200'
            else:
                resp['message'] = 'This checkout paid'
                return HttpResponse(json.dumps(resp), content_type='application/json')
        except:
            resp['message'] = 'Not found'
    if request.method == 'GET':
        username = request.GET.get("username")
        if username:
            resp['data'] = list(PaymentModel.objects.filter(
                username=username).values())
            resp['status'] = 'Success'
            resp['status_code'] = '200'
    if request.method == 'DELETE':
        id = request.GET.get("id")
        if id:
            try:
                ca = PaymentModel.objects.get(id=id)
                if ca:
                    ca.delete()
                    resp['status'] = 'Success'
                    resp['status_code'] = '200'
            except:
                resp['data'] = 'Not found'
# If a user is not found then it give failed as response.
    return HttpResponse(json.dumps(resp), content_type='application/json')

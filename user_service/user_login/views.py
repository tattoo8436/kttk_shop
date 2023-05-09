# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from user_model.models import UserModel
def user_validation(uname, password):
    user_data = UserModel.objects.filter(email = uname, password = password)
    if user_data:
        return "Valid User" 
    else:
        return "Invalid User"
    
@csrf_exempt
def user_login(request):
    uname = request.POST.get("username")
    password = request.POST.get("pass")
    resp = {}
    if uname and password:
        respdata = user_validation(uname, password)
        if respdata == "Valid User":
            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['message'] = 'Welcome to Ecommerce website......'
        elif respdata == "Invalid User":
            resp['status'] = 'Failed'
            resp['status_code'] = '400'
            resp['message'] = 'Invalid credentials.'
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'All fields are mandatory.'
    return HttpResponse(json.dumps(resp), content_type = 'application/json')






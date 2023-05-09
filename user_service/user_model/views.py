# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from user_model.models import UserModel
from user_info.views import user_data

### This function is inserting the data into our table.
def data_insert(fname, lname, email, mobile, password, address):
    user_data = UserModel(fname = fname, lname = lname, email =
    email, mobile = mobile, password = password, address = address)
    user_data.save()
    return 1

@csrf_exempt
def change_pass(request):
    email = request.POST.get("username")
    password = request.POST.get("pass")
    newpassword = request.POST.get("newpass")
    resp = {}

    if email and password and newpassword:
        user = user_data(email) 
        if user and user.get('password') == password:
            user.update(password = newpassword)
            resp['status'] = 'Success'
            resp['status_code'] = '200'
        else:
            resp['status'] = 'Failed'
            resp['status_code'] = '400'
            resp['message'] = 'Check old password'
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'All fields are mandatory.'
    return HttpResponse(json.dumps(resp), content_type = 'application/json')

### This function will get the data from the front end.
@csrf_exempt
def registration_req(request):
### The Following are the input fields.
    fname = request.POST.get("fname")
    lname = request.POST.get("lname")
    email = request.POST.get("email")
    mobile = request.POST.get("phone")
    password = request.POST.get("pass")
    cnf_password = request.POST.get("pass2")
    address = request.POST.get("address")
    resp = {}
    if fname and lname and email and mobile and password and cnf_password and address:
        if not user_data(email):
            if len(str(mobile)) == 10:  
                if password == cnf_password:
                    respdata = data_insert(fname, lname, email, mobile, password, address)
                    if respdata:
                        resp['status'] = 'Success'
                        resp['status_code'] = '200'
                        resp['message'] = 'User is registered Successfully.'
                    else:
                        resp['status'] = 'Failed'
                        resp['status_code'] = '400'
                        resp['message'] = 'Unable to register user, Please try again.'
                else:
                    resp['status'] = 'Failed'
                    resp['status_code'] = '400'
                    resp['message'] = 'Password and Confirm Password should be same.'
            else:
                resp['status'] = 'Failed'
                resp['status_code'] = '400'
                resp['message'] = 'Mobile Number should be 10 digit.'
        else:
            resp['status'] = 'Failed'
            resp['status_code'] = '400'
            resp['message'] = 'Email existed'
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'All fields are mandatory.'
    return HttpResponse(json.dumps(resp), content_type = 'application/json')
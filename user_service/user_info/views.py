# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import status
from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from requests import Response
from user_model.models import UserModel as userreg
from user_model.models import UserRole
from rest_framework import generics
from rest_framework.decorators import api_view
from user_model.models import Role, RoleSerializer

# This function is for fetching the user data.


def user_data(uname):
    user = userreg.objects.filter(email=uname)
    for data in user.values():
        return data


@csrf_exempt
def user_info(request):
    uname = json.loads(request.body).get('username')
    resp = {}
    if request.method == 'POST':
        print(uname)
        if uname:
            respdata = user_data(uname)
            print(respdata)
            dict1 = {}
            if respdata:
                dict1['fname'] = respdata.get('fname')
                dict1['lname'] = respdata.get('lname')
                dict1['mobile'] = respdata.get('mobile')
                dict1['email'] = respdata.get('email')
                dict1['address'] = respdata.get('address')
            if dict1:
                resp['status'] = 'Success'
                resp['status_code'] = '200'
                resp['data'] = dict1
            else:
                resp['status'] = 'Failed'
                resp['status_code'] = '400'
                resp['message'] = 'User Not Found.'
        else:
            resp['status'] = 'Failed'
            resp['status_code'] = '400'
            resp['message'] = 'Fields is mandatory.'
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Request type is not matched.'
    print(resp)
    return HttpResponse(json.dumps(resp), content_type='application/json')


@api_view(['GET', 'DELETE', 'POST'])
def UserRoleDetail(request):
    resp = {}
    resp['status'] = 'Success'
    resp['status_code'] = '200'
    if request.method == 'GET':
        role = request.GET.get('role')
        email = request.GET.get('username')
        if (role and email):
            i = UserRole.objects.filter(role=role, email=email).count()
            if i > 0:
                resp['data'] = True
            else:
                resp['data'] = False
        elif email:
            resp['data'] = list(
                UserRole.objects.filter(email=email).values_list('role', flat=True))
        elif role:
            resp['data'] = list(
                UserRole.objects.filter(role=role).values_list('email', flat=True))
        else:
            resp['data'] = [role for role in UserRole.objects.all().values()]

    else:
        email = json.loads(request.body).get('username')
        role = json.loads(request.body).get('role')
        actor = json.loads(request.body).get('actor')
        if UserRole.objects.filter(role='QuanLy', email=actor).count() == 0:
            resp['status'] = 'Failed'
            resp['status_code'] = '400'
            resp['message'] = 'Not permission'
            return HttpResponse(json.dumps(resp), content_type='application/json')

        if request.method == 'POST':
            if not email or not role:
                resp['status'] = 'Failed'
                resp['status_code'] = '400'
                resp['message'] = 'Fields is mandatory.'
            elif Role.objects.filter(role=role).count() == 0 or userreg.objects.filter(email=email).count() == 0:
                resp['status'] = 'Failed'
                resp['status_code'] = '400'
                resp['message'] = 'Role or username not existed'
            if UserRole.objects.filter(role=role, email=email).count() == 0:
                r = UserRole(role=role, email=email)
                r.save()
            else:
                resp['status'] = 'Failed'
                resp['status_code'] = '400'
                resp['message'] = 'Existed'
        if request.method == 'DELETE':
            Role.objects.filter(role=role).delete()
            UserRole.objects.filter(role=role).delete()
            resp['data'] = role
    return HttpResponse(json.dumps(resp), content_type='application/json')


@api_view(['GET', 'DELETE', 'POST'])
def role_detail(request):
    resp = {}
    resp['status'] = 'Success'
    resp['status_code'] = '200'
    if request.method == 'GET':
        resp['data'] = list(Role.objects.values_list('role', flat=True))
    else:
        role = json.loads(request.body).get('role')
        actor = json.loads(request.body).get('actor')
        if UserRole.objects.filter(role='QuanLy', email=actor).count() == 0:
            resp['status'] = 'Failed'
            resp['status_code'] = '400'
            resp['message'] = 'Not permission'
            return HttpResponse(json.dumps(resp), content_type='application/json')
        if request.method == 'POST':
            r = Role(role=role)
            r.save()
            resp['data'] = role
        if request.method == 'DELETE':
            Role.objects.filter(role=role).delete()
            UserRole.objects.filter(role=role).delete()
            resp['data'] = role
    return HttpResponse(json.dumps(resp), content_type='application/json')

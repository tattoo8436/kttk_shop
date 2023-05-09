# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from product_model.models import Product, Book, Shoes, Clothes
@csrf_exempt
def get_product_data(request):
    data = []
    resp = {}
    prodata = Product.objects.all()
    for tbl_value in prodata.values():
        product = tbl_value
        category = product.get('category')
        if category == "book":
            product['author'] = Book.objects.filter(
                productId=product.get('id')).values().first().get('author')
        if category == "shoes":
            product['size'] = Shoes.objects.filter(
                productId=product.get('id')).values().first().get('size')
        if category == "clothes":
            product['size'] = Clothes.objects.filter(
                productId=product.get('id')).values().first().get('size')
            resp['data'] = product
        data.append(product)
    if data:
        resp['status'] = 'Success'
        resp['status_code'] = '200'
        resp['data'] = data
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Data is not available.'
    return HttpResponse(json.dumps(resp), content_type='application/json')


@csrf_exempt
def product(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        category = body.get("category")
        name = body.get("name")
        quantity = body.get("quantity")
        price = body.get("price")

        resp = {'category': category, 'name': name,
                'quantity': quantity, 'price': price}
        prodata = Product(category=category, quantity=quantity,
                          price=price)
        category = category.lower().strip()
        prodata.save()
        resp['id'] = prodata.id
        if category == "book":
            Book(productId=prodata.id, name=name,
                 author=body.get("author")).save()
            resp['author'] = body.get("author")
        if category == "shoes":
            Shoes(productId=prodata.id, name=name,
                   size=body.get("size")).save()
            resp['size'] = body.get("size")
        if category == "clothes":
            Clothes(productId=prodata.id, name=name,
                    size=body.get("size")).save()
            resp['size'] = body.get("size")
        resp['status'] = 'Success'
        resp['status_code'] = '200'
        return HttpResponse(json.dumps(resp), content_type='application/json')

    if request.method == 'GET':
        resp = {}
        productId = request.GET.get('productId')
        if not Product.objects.filter(id=productId).values():
                resp['status'] = 'Fail'
                resp['status_code'] = '400'
                resp['message'] = 'Not found'
                return HttpResponse(json.dumps(resp), content_type='application/json')
        for p in Product.objects.filter(id=productId).values():
            product = p
            category = p.get('category')
            if category == "book":
                product['author'] = Book.objects.filter(
                    productId=productId).values().first().get('author')
            if category == "shoes":
                product['size'] = Shoes.objects.filter(
                    productId=productId).values().first().get('size')
            if category == "clothes":
                product['size'] = Clothes.objects.filter(
                    productId=productId).values().first().get('size')
            resp['data'] = product
        resp['status'] = 'Success'
        resp['status_code'] = '200'
        return HttpResponse(json.dumps(resp), content_type='application/json')

    if request.method == 'DELETE':
        resp = {}
        productId = request.GET.get('productId')
        Product.objects.filter(id=productId).delete()
        resp['status'] = 'Success'
        resp['status_code'] = '200'
        return HttpResponse(json.dumps(resp), content_type='application/json')

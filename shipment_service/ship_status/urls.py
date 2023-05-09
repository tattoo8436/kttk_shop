from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('shipment_status/', views.useShipment, name='shipment_status'),
    path('shipment_updates/', views.changeShip, name='shipment_reg_update'),
]
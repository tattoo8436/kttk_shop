from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('payment/', views.usePayment, name='usePayment'),
    path('pay-ok/', views.pay, name='pay'),
]
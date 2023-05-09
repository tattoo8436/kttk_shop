from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.useCart),
    path('check/', views.getTotalPrice),
    path('checkout/', views.add),
]

from django.urls import path,re_path
from django.shortcuts import HttpResponse,render,redirect
from django.http import JsonResponse
from django.conf.urls import  include

from app01 import  views
urlpatterns = [
    path('index_db/',views.index_db),
]